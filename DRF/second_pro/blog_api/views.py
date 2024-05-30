from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import BlogSerializers
from .models import AllBlogs

# Create your views here.
@api_view(['GET', 'POST'])
def all_blogs(request):
    if request.method == 'GET':
        all_data = AllBlogs.objects.all()
        se = BlogSerializers(all_data, many=True)
        return Response(data = se.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        se = BlogSerializers(data = request.data)
        if se.is_valid():
            se.save()
            return Response(data = se.data, status = status.HTTP_201_CREATED)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def blog_details(request, id):
    try:
        blog = AllBlogs.objects.get(id=id)
    except AllBlogs.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        se = BlogSerializers(blog)
        return Response(data = se.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        se = BlogSerializers(blog, data = request.data)
        if se.is_valid():
            se.save()
            return Response(data = se.data, status = status.HTTP_200_OK)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        se = BlogSerializers(blog, data = request.data, partial = True)
        if se.is_valid():
            se.save()
            return Response(data = se.data, status = status.HTTP_202_ACCEPTED)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)