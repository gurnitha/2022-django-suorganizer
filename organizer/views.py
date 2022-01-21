# organizer/views.py

# Django modules
from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.shortcuts import get_object_or_404

# Locals
from organizer.models import Startup, Tag

# Create your views here.


def StartupListView(request):
    startup_list = Startup.objects.all()
    context = {
        'startup_list': startup_list
    } 
    return render(request, 'organizer/startup_list.html', context)


def StartupDetailView(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)

    context = {
        'startup': startup
    } 
    return render(request, 'organizer/startup_detail.html', context)


def TagListView(request):
    tag_list = Tag.objects.all()
    context = {
        'tag_list': tag_list
    }
    return render(request, 'organizer/tag_list.html', context)


def TagDetailView(request, slug):
    try:
        tag = Tag.objects.get(slug__iexact=slug)
        # tag = get_object_or_404(Tag, slug__iexact=slug)
    except Tag.DoesNotExist:
        return HttpResponse('<h1>Tag not found!</h1>')
    context = {
        'tag': tag
    }
    return render(request, 'organizer/tag_detail.html', context)



