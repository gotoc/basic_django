from django.contrib import admin
from jraywo.models import Category, Entry, Link

class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

class CategoryAdmin(admin.ModelAdmin):
    ordering = ['title']
    prepopulated_fields = {'slug': ['title']}

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)
