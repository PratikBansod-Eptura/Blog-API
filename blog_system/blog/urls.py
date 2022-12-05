from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('blogs/', views.blog_list, name='blogs'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('user-create/', views.register_user, name='user-create'),
    path('unapproved-blogs/', views.unapproved_blogs, name='unapproved-blog'),
    path('blog-approve/<int:pk>/', views.blog_approve, name='blog-approve'),
    path('blog-approve/', views.blog_approve, name='blog-approve'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]