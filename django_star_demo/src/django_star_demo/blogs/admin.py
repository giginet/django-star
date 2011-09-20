# -*- coding: utf-8 -*-
#    
#    django_star_demo.blogs.admin
#    created by giginet on 2011/09/20
#
from django.contrib import admin

from models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'body',)
admin.site.register(Entry, EntryAdmin)