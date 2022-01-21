# blog/views/py

# Django modules
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Locals
from blog.models import Post

# Create your views here.

def PostListView(request):
    post_list = Post.objects.all()
    context = {
        'post_list':post_list
    }
    return render(request, 'blog/post_list.html', context)
    

def PostDetailView(request, year, month, slug):
    post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug)
    context = {
        'post':post
    }
    return render(request, 'blog/post_detail.html', context)
