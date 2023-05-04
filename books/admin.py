from re import search
from django.contrib import admin
from .models import Books

class AdminBooks(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year', 'descripition')
    search_fields = ['title']
    list_display_links = ['title']

admin.site.register(Books)