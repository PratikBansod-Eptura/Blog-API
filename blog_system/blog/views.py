from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer


# Create your views here.
@api_view()
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        print(f'\nserilizer data = {serializer.data}\n')
        return Response(serializer.data)