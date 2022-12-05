from django.contrib import admin
from .models import Blog, CustomUser

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title', 'description', 'published_date', 'published_date', 'last_updated_on', 'approval_status',]


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]