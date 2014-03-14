from django.conf.urls import *
from django.contrib import flatpages
from django.views.generic.base import TemplateView

 
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', include('jeffreyvwong.urls.home')),    

    url(r'^bio/$', TemplateView.as_view(template_name='jeffreyvwong/bio.html'), name='jeffreyvwong_bio'),
    url(r'^skills/$', TemplateView.as_view(template_name='jeffreyvwong/skills.html'), name='jeffreyvwong_skills'),
    url(r'^cv/$', TemplateView.as_view(template_name='jeffreyvwong/resume.html'), name='jeffreyvwong_cv'),
    url(r'^contact/$', TemplateView.as_view(template_name='jeffreyvwong/contact.html'), name='jeffreyvwong_contact'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^visualization/', include('jeffreyvwong.urls.visualization')),
    url(r'^modelling/$', TemplateView.as_view(template_name='jeffreyvwong/modelling.html'), name='jeffreyvwong_modelling'),
    url(r'^learning/', include('jeffreyvwong.urls.learning')),
    url(r'^publications/', TemplateView.as_view(template_name='jeffreyvwong/publication.html'), name='jeffreyvwong_publication'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()


