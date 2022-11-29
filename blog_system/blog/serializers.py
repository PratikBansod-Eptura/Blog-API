from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['user', 'title', 'description', 'published_date', 'published_date', 'last_updated_on', 'approval_status',]
