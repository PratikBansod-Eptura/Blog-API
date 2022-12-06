from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # blog related endpoints
    path("blogs/", views.blog_list, name="blogs"),
    path("blog-create/", views.blog_create, name="blog-create"),
    path("blog-detail/", views.blog_detail, name="blogs-detail"),

    # user related endpoints
    path("user-create/", views.register_user, name="user-create"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

    # Admin related endpoints
    path("unapproved-blogs/", views.unapproved_blogs, name="unapproved-blog"),
    path("blog-approve/", views.blog_approve, name="blog-approve"),
]
