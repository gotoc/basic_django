from django.conf.urls import *
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView

from jraywo.models import Link
 
urlpatterns = patterns('',
    url(r'^$', ArchiveIndexView.as_view(model=Link,
                                        date_field='pub_date',
                                        allow_empty = True,
                                        paginate_by = 5), name='jraywo_link_archive_index'), 
    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(model=Link,
                                                       date_field='pub_date',
                                                       make_object_list=True,
                                                       allow_empty = True,
                                                       paginate_by = 5), name='jraywo_link_archive_year'), 
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthArchiveView.as_view(model=Link,
                                                                         date_field='pub_date',
                                                                         allow_empty = True,
                                                                         paginate_by = 5),name='jraywo_link_archive_month'), 
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', DayArchiveView.as_view(model=Link,
                                                                                      date_field='pub_date',
                                                                                      allow_empty = True,
                                                                                      paginate_by = 5), name='jraywo_link_archive_day'), 
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(model=Link,
                                                                                                       date_field='pub_date'), name='jraywo_link_detail'),
)