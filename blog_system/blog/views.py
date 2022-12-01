from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer, CustomUserSignupSerializer
from rest_framework import status

# Create your views here.
# @api_view()
# def blog_list(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         print(f'\nserilizer data = {serializer.data}\n')
#         return Response(serializer.data, status.HTTP_200_OK)
#
# @api_view(['POST'])
# def blog_create(request):
#     if request.method == 'POST':
#         serializer = BlogSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {'message':'Blog created successfully'}
#             return Response(response, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        print(f'\nserilizer data = {serializer.data}\n')
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method=='POST':
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = BlogSerializer(blog, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog.delete()
        return Response({'message':'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def register_user(request):
    serializer = CustomUserSignupSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Signup successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_201_CREATED)