from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'published_date', 'published_date', 'last_updated_on', 'approval_status',]
