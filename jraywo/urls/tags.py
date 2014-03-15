from django.conf.urls import *
from django.views.generic import ListView

from jraywo.models import Entry, Link

from jraywo.views import ModelByTagListView
from tagging.models import Tag
 
urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Tag,
                                template_name='jraywo/tag_list.html',
                                allow_empty = True), name='tag_list'),
    url(r'^entries/(?P<tag>[-\w]+)/$', ModelByTagListView.as_view(template_name='jraywo/entries_by_tag.html',
                                                                  allow_empty = True,
                                                                  paginate_by = 5),
                                                                  kwargs={'queryset_or_model': Entry.live.all() },
                                                                  name='jraywo_entry_archive_tag'),   
    url(r'^links/(?P<tag>[-\w]+)/$', ModelByTagListView.as_view(template_name='jraywo/links_by_tag.html',
                                                                allow_empty = True,
                                                                paginate_by = 5),
                                                                kwargs={'queryset_or_model': Link},
                                                                name='jraywo_link_archive_tag'),   
)
