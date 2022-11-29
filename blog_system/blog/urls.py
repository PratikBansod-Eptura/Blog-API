from django.urls import path
from .views import blog_list

urlpatterns = [
    path('blogs/', blog_list, name='blogs')
]