from rest_framework import serializers
from .models import Blog, CustomUser


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','user', 'title', 'description', 'published_date', 'published_date', 'last_updated_on', 'approval_status',]


class CustomUserSignupSerializer(serializers.ModelSerializer):
    #confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username','password', 'email', 'gender', 'mob_number']
