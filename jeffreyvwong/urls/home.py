from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.contrib import flatpages
from django.views.generic.base import TemplateView
from jeffreyvwong.sitemaps import SnippetSitemap, PageSitemap

from jeffreyvwong.views import RobotsView

sitemaps = {
    'snippets': SnippetSitemap(),
    'pages': PageSitemap([ 'jeffreyvwong_home'
                        ,  'jeffreyvwong_bio'
                        ,  'jeffreyvwong_skills'
                        ,  'jeffreyvwong_cv'
                        ,  'jeffreyvwong_contact'
                        ,  'jeffreyvwong_modelling'
                        ,  'jeffreyvwong_publication'
                        ])
}

urlpatterns = patterns('')

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns = patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',

    url(r'^$', TemplateView.as_view(template_name='jeffreyvwong/home.html'), name='jeffreyvwong_home'),

    url(r'^bio/$',     TemplateView.as_view(template_name='jeffreyvwong/bio.html'),     name='jeffreyvwong_bio'),
    url(r'^skills/$',  TemplateView.as_view(template_name='jeffreyvwong/skills.html'),  name='jeffreyvwong_skills'),
    url(r'^cv/$',      TemplateView.as_view(template_name='jeffreyvwong/cv.html'),      name='jeffreyvwong_cv'),
    url(r'^contact/$', TemplateView.as_view(template_name='jeffreyvwong/contact.html'), name='jeffreyvwong_contact'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^visualization/', include('jeffreyvwong.urls.visualization')),
    url(r'^modelling/$',    TemplateView.as_view(template_name='jeffreyvwong/modelling.html'), name='jeffreyvwong_modelling'),
    url(r'^publications/$',  TemplateView.as_view(template_name='jeffreyvwong/publication.html'), name='jeffreyvwong_publication'),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots\.txt$', RobotsView.as_view(), name='robots')
)

