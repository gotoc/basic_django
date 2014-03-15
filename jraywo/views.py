from django.shortcuts import get_object_or_404, render_to_response
from jraywo.models import Entry
from django.views.generic import ListView
from jraywo.models import Category
from tagging.models import Tag, TaggedItem
import logging
#~ logging.basicConfig(filename='weblog.log', level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

class EntryByCategoryListView(ListView):
    
    def get_queryset(self):
        model = self.kwargs['model']
        self.slug_query = get_object_or_404(model, slug=self.kwargs['slug'])
        return self.slug_query.live_entry_set()
    
    def get_context_data(self, **kwargs):
        context = super(EntryByCategoryListView, self).get_context_data(**kwargs)
        context['model'] = self.slug_query
        return context
        
class ModelByTagListView(ListView):
    
    def get_queryset(self):
        queryset_or_model = self.kwargs['queryset_or_model']
        self.tag_query = Tag.objects.get(name=self.kwargs['tag'])
        return TaggedItem.objects.get_by_model(queryset_or_model, self.tag_query)
        
    def get_context_data(self, **kwargs):
        context = super(ModelByTagListView, self).get_context_data(**kwargs)
        context['tag'] = self.tag_query
        return context

 




   


