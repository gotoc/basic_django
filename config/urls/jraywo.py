from django.conf.urls import patterns, include, url
from django.contrib import flatpages
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',

    url(r'^admin/?', include(admin.site.urls)),
    url(r'^', include('jraywo.urls.home')),

    ##don't do this in production
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/home/jvwong/projects/django_projects/static/' }),

)

