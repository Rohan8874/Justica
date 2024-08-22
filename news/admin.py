from django.contrib import admin
from .models import NewsItem

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'category', 'author')
    search_fields = ('title', 'category', 'author')
    list_filter = ('date', 'category')
