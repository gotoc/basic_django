import datetime

from django.contrib.auth.models import User
from django.db import models

from markdown import markdown
from tagging.fields import TagField

from django.conf import settings

class Link(models.Model):
    
    #Core fields
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    #Fields to store generated HTML
    descripton_html = models.TextField(editable=False, blank=True)
    
    #Meta data 
    posted_by = models.ForeignKey(User)
    slug = models.SlugField(unique_for_date='pub_date')
    
    #Source info 
    via_name = models.CharField('Via', max_length=250, blank=True, help_text='The name of the person whose site you spotted the link on (Optional)' )
    via_url = models.URLField('Via', max_length=250, blank=True, help_text='The URL of the site you spotted the link on (Optional)' )

    #actions
    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to Delicious', default=True, help_text='If checked, this link will be posted both to your weblog and your del.icio.us account.')
    
    #Categorization
    tags = TagField()
    
    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.title

    def save(self):
        if self.description:
            self.description_html = markdown(self.description)
        if not self.id and self.post_elsewhere:
            import pydelicious
            from django.utils.encoding import smart_str
            pydelicious.add(settings.DELICIOUS_USER,
                            settings.DELICIOUS_PASSWORD,
                            smart_str(self.url),
                            smart_str(self.title),
                            smart_str(self.tags)
                           )
        super(Link, self).save()

    @models.permalink    
    def get_absolute_url(self):
        return ('jraywo_link_detail', (), {'year':  self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug}) 

class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def live_entry_set(self):
        from jraywo.models import Entry
        return self.entry_set.filter(status=Entry.LIVE_STATUS)
        
    class Meta:
        verbose_name_plural = "Categories"
        
    def __unicode__(self):
        return self.title
    
   
class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),          
    )
    #Core fields
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank = False)
    body = models.TextField(blank = False)
    entry_tease = models.ImageField( upload_to = 'entry', null=True, blank=True )
    
    #Fields to store generated HTML
    excerpt_html = models.TextField(editable=False)
    body_html = models.TextField(editable=False)
    
    #Meta data 
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured =  models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date')
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    pub_date = models.DateTimeField(editable = False)
    updated_date = models.DateTimeField(editable = False)
    
    #Categorization
    categories = models.ManyToManyField(Category, blank = True)
    tags = TagField(help_text = "Separate tags with spaces.")
     
    # Need to be this way around so that non-live entries will show up in Admin, which uses the default (first) manager.
    objects = models.Manager()
    live = LiveEntryManager()
      
    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert = False, force_update = False):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        self.excerpt_html = markdown(self.excerpt)
        self.body_html = markdown(self.body)
        super(Entry, self).save(force_insert, force_update)
   
    @models.permalink    
    def get_absolute_url(self):
        return ('jraywo_entry_detail', (), {'year':  self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug})
                                              


from akismet import Akismet
from django.conf import settings
from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib.sites.models import Site
from django.utils.encoding import smart_str

class EntryModerator(CommentModerator):
    auto_moderate_field = 'pub_date'
    moderate_after = 30
    email_notification = True
    
    def moderate (self, comment, content_object, request):
        already_moderated = super(EntryModerator, self).moderate(comment, content_object, request)
        if already_moderated:
            return True
        akismet_api = Akismet(key=settings.AKISMET_API_KEY, blog_url="http:/%s/" %Site.objects.get_current().domain)
        if akismet_api.verify_key():
            akismet_data = { 'comment_type': 'comment',
                             'referrer': request.META['HTTP_REFERER'],
                             'user_ip': comment.ip_address,
                             'user-agent': request.META['HTTP_USER_AGENT'] }
            return akismet_api.comment_check(smart_str(comment.comment),
                                akismet_data,
                                build_data=True)
        return False
        
moderator.register(Entry, EntryModerator)
