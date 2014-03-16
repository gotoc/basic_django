from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import flatpages
from django.views.generic.base import TemplateView


#from jeffreyvwong.sitemap import SnippetSitemap
#info_dict = {
#    'queryset': Snippet.objects.all(),
#    'date_field': 'updated_date',
#}
#sitemaps = {
#    'snippets': SnippetSitemap(),
#}

import logging

from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',

    url(r'^$', include('jeffreyvwong.urls.home')),

    url(r'^bio/$', TemplateView.as_view(template_name='jeffreyvwong/bio.html'), name='jeffreyvwong_bio'),
    url(r'^skills/$', TemplateView.as_view(template_name='jeffreyvwong/skills.html'), name='jeffreyvwong_skills'),
    url(r'^cv/$', TemplateView.as_view(template_name='jeffreyvwong/cv.html'), name='jeffreyvwong_cv'),
    url(r'^contact/$', TemplateView.as_view(template_name='jeffreyvwong/contact.html'), name='jeffreyvwong_contact'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^visualization/', include('jeffreyvwong.urls.visualization')),
    url(r'^modelling/$', TemplateView.as_view(template_name='jeffreyvwong/modelling.html'), name='jeffreyvwong_modelling'),
    url(r'^learning/', include('jeffreyvwong.urls.learning')),
    url(r'^publications/', TemplateView.as_view(template_name='jeffreyvwong/publication.html'), name='jeffreyvwong_publication'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),

 #   url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)


