from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blogs/', views.all_blogs, name='all_blogs'),
    path('edit_blog/<int:id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog')
]