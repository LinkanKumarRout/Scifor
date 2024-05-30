from django.shortcuts import render
from .models import AllBlogs
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def all_blogs(request):
    if request.method == "GET":
        data = AllBlogs.objects.all()
        se = BlogSerializer(data, many = True)
        return Response(data = se.data, status= status.HTTP_200_OK)
    elif request.method == "POST":
        se = BlogSerializer(data = request.data)
        if se.is_valid():
            se.save()
            return Response(data = se.data, status = status.HTTP_201_CREATED)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def blog_details(request, id):
    try:
        data = AllBlogs.objects.get(id=id)
    except AllBlogs.DoesNotExist:
        return Response(satus = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        se = BlogSerializer(data)
        return Response(data = se.data, status= status.HTTP_200_OK)
    elif request.method == 'PUT':
        se = BlogSerializer(data, request.data)
        if se.is_valid():
            se.save()
            return Response(data = se.data, status = status.HTTP_200_OK)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        se = BlogSerializer(data, request.data, partial = True)
        if se.is_valid():
            se.save()
            return Response(data = se.data, status = status.HTTP_202_ACCEPTED)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)