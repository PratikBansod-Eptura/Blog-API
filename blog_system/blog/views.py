from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status

# Create your views here.
@api_view()
def blog_list(request, id = None):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        print(f'\nserilizer data = {serializer.data}\n')
        return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST'])
def blog_create(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'Blog created successfully'}
            return Response(response, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)