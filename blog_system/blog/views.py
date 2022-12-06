from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Blog, CustomUser
from .serializers import BlogSerializer, CustomUserSignupSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination


# Create your views here.
@api_view()
def blog_list(request):
    """
    Returns approved blogs..

    Authentication not required.
    """
    if request.method == 'GET':
        print(request.query_params.get('id'))
        if request.query_params.get('id'):
            try:
                blog = Blog.objects.get(
                                        pk=request.query_params.get('id'),
                                        approval_status = True
                                        )
            except Blog.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = BlogSerializer(blog)
            return Response(serializer.data, status.HTTP_200_OK)
        print(f'\nrequest.user = {request.user}\n')
        blogs_queryset = Blog.objects.filter(approval_status = True)

        # Pagination code
        paginator = PageNumberPagination()
        paginator.page_size = 3
        blogs = paginator.paginate_queryset(blogs_queryset, request)

        serializer = BlogSerializer(blogs, many=True)
        print(f'\nserilizer data = {serializer.data}\n')
        return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def blog_create(request):
    """
    Create blog - Only authenticated user can create blog.
    """
    if request.method == 'POST':
        serializer = BlogSerializer(
                                    context = {'request':request},
                                    data = request.data
                                    )
        print(f'\nrequest.user = {request.user}\n')
        if serializer.is_valid():
            serializer.save()
            #response = {'message':'Blog created successfully'}
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','PATCH','DELETE'])
@permission_classes((IsAuthenticated,))
def blog_detail(request):
    """
    Blog can be fully or partially updated by admin or respective user.
    """
    blog_id = request.query_params.get('id')

    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user_obj = CustomUser.objects.get(username = request.user)

    # Either admin or respective user of blog can update and delete the Blog
    if blog.user == user_obj or request.user.username == 'admin':
        if request.method == 'PUT':
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
            print(f'\n UInside DELETE method\n')
            blog.delete()
            return Response(
                            {'message':'Blog deleted successfully'},
                            status=status.HTTP_204_NO_CONTENT
                            )
    return Response(
                    {'message':'Can only update your blog'},
                    status=status.HTTP_400_BAD_REQUEST
                    )


@api_view(['POST'])
def register_user(request):
    """
    Create user profile.
    """
    serializer = CustomUserSignupSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
                        {"message":"Signup successfully"},
                        status=status.HTTP_201_CREATED
                        )
    return Response(serializer.errors, status=status.HTTP_201_CREATED)


@api_view()
@permission_classes((IsAdminUser, ))
def unapproved_blogs(request):
    """
    Returns only unapproved blogs.

    Only admin can access this view.
    """
    try:
        blogs = Blog.objects.filter(approval_status = False)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(f'blogs = {blogs}')
    if len(blogs)!=0:
        serializer = BlogSerializer(blogs, many=True)
        response = serializer.data
    else:
        response = {'message':'No blog for approval'}
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def blog_approve(request):
    """"
    Approve unapproved blog for publication.

    Only admin have access og this view.
    """
    blog_id = request.query_params.get("id")
    print(f'blog_id = {blog_id}')
    blog = Blog.objects.get(pk=blog_id)
    print(f'\n blog = {blog}\n')
    blog.approval_status = True
    blog.save()
    return Response(
                    {'message':'blog is successfully approved for publication'},
                    status=status.HTTP_200_OK
                    )