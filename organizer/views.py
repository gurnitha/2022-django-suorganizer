# organizer/views.py

# Django modules
from django.shortcuts import render
from django.http.response import HttpResponse, Http404

# Locals
from organizer.models import Startup, Tag

# Create your views here.


def HomePageView(request):
    startup_list = Startup.objects.all()
    context = {
        'startup_list': startup_list
    }
    return render(request, 'organizer/startup_list.html', context)



def TagDetailView(request, slug):
    try:
        tag = Tag.objects.get(slug__iexact=slug)
    except Tag.DoesNotExist:
        return HttpResponse('<h1>Tag not found!</h1>')

    context = {
        'tag': tag
    }
    return render(request, 'organizer/tag_detail.html', context)



def TagListView(request):
    tag_list = Tag.objects.all()
    context = {
        'tag_list': tag_list
    }
    return render(request, 'organizer/tag_list.html', context)


