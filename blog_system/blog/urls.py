from django.urls import path
from .views import blog_list, blog_create

urlpatterns = [
    path('blogs/', blog_list, name='blogs'),
    path('blog-create/', blog_create, name='blog-create')
]