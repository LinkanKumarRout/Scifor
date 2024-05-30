from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from .serializers import PostSerializers
from rest_framework.response import Response
from rest_framework import status


URL = "https://jsonplaceholder.typicode.com/posts/"

@api_view(['GET', 'POST'])
def all_post(request):
    if request.method == 'GET':
        response = requests.get(URL)
        return Response(data = response.json(), status = response.status_code)
    elif request.method == 'POST':
        se = PostSerializers(data = request.data)
        if se.is_valid():
            response = requests.post(URL, json= se.validated_data)
            return Response(data = response.json(), status = response.status_code)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_details(request, id):
    if request.method == 'GET':
        response = requests.get(f"{URL}{id}")
        return Response(data = response.json(), status = response.status_code)
    if request.method == 'PUT':
        se = PostSerializers(data = request.data)
        if se.is_valid():
            response = requests.put(f"{URL}{id}", json = se.validated_data)
            return Response(data = response.json(), status = response.status_code)
        return Response(data = se.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        se = PostSerializers(data = request.data, partial = True)
        if se.is_valid():
            response = requests.patch(f"{URL}{id}", json = se.validated_data)
            return Response(data = response.json(), status = response.status_code)
        return Response(data = se.errors, status= status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        response = requests.delete(f"{URL}{id}")
        return Response(status= response.status_code)