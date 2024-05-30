from django.urls import path
from . import views

urlpatterns = [
    path('download', views.youtube_download, name='youtube')
]