from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def main(request):
    return render(request, 'home.html')

def all_blogs(request):
    blogs = AllBlogs.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'all_blogs.html', context)

def edit_blog(request, id):
    blog = AllBlogs.objects.get(id=id)
    context = {
        'blog':blog
    }
    if request.method == 'GET':
        return render(request, 'edit_blog.html', context)
    else:
        blog.title = request.POST['title']
        blog.description = request.POST['description']
        blog.image = request.POST['image']
        blog.save()
        return redirect('all_blogs')

def delete_blog(request, id):
    blog = AllBlogs.objects.get(id=id)
    blog.delete()
    return redirect('all_blogs')