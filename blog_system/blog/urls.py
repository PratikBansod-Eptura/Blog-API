from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blogs'),
    path('blogs/<int:pk>', views.blog_detail, name='blog-detail')
]