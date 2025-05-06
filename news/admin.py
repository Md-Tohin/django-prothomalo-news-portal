from django.contrib import admin
from .models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'category', 'is_read', 'is_discussed', 'is_selected', 'is_image', 'is_top', 'is_publish', 'modified_date')
    prepopulated_fields = {'slug': ('news_title',)}

admin.site.register(News, NewsAdmin)


