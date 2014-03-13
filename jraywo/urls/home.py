from django.conf.urls import *
from django.views.generic.base import TemplateView
 
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='jraywo/home.html'), name='jraywo_home'),
)


