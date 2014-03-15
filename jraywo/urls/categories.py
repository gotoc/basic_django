from django.conf.urls import *
from django.views.generic import ListView

from coltrane.models import Category
from coltrane.views import EntryByCategoryListView

urlpatterns = patterns('coltrane.views',
    url(r'^$', ListView.as_view(model=Category), name='category_list'), 
    url(r'^(?P<slug>[-\w]+)/$', EntryByCategoryListView.as_view(template_name = 'coltrane/category_detail.html',
                                                                paginate_by = 5,
                                                                allow_empty = True), kwargs = { 'model': Category }, name='category_detail'), 
)
