# organizer/views.py

# Django modules
from django.shortcuts import render

# Locals
from organizer.models import Startup, Tag

# Create your views here.


def HomePageView(request):
    startup_list = Startup.objects.all()
    
    context = {
        'startup_list': startup_list
    }

    return render(request, 'organizer/startup_list.html', context)



def TagListView(request):
    tag_list = Tag.objects.all()
    
    context = {
        'tag_list': tag_list
    }

    return render(request, 'organizer/tag_list.html', context)


