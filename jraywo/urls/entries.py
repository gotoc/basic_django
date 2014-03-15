from django.conf.urls import *
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from coltrane.models import Entry

urlpatterns = patterns('',
    url(r'^$', ArchiveIndexView.as_view( queryset = Entry.live.all(),
                                         date_field = 'pub_date',
                                         allow_empty = True,
                                         paginate_by = 5,
                                        ), name='coltrane_entry_archive_index'), 
    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(queryset = Entry.live.all(),
                                                       date_field='pub_date',
                                                       allow_empty = True,
                                                       make_object_list=True), name='coltrane_entry_archive_year'), 
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthArchiveView.as_view(queryset = Entry.live.all(),
                                                                         date_field = 'pub_date',
                                                                         allow_empty = True,
                                                                         paginate_by = 5,
                                                                         ), name='coltrane_entry_archive_month'), 
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', DayArchiveView.as_view(queryset = Entry.live.all(),
                                                                                      date_field = 'pub_date',
                                                                                      allow_empty = True,
                                                                                       paginate_by = 5,
                                                                                      ), name='coltrane_entry_archive_day'), 
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(queryset = Entry.live.all(),
                                                                                                       date_field = 'pub_date',
                                                                                                       ), name='coltrane_entry_detail'),
        
)
