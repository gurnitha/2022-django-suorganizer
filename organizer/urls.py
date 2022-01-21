# organizer/urls.py

# Django modules
from django.conf.urls import url
from django.urls import path

from organizer.views import (
    StartupListView, TagListView, 
    TagDetailView)

app_name = 'organizer'

urlpatterns = [
    path('startups/', StartupListView, name='startuplist'),
    path('tags/', TagListView, name='taglist'),
    path('tag/<str:slug>/', TagDetailView, name='tagdetail'),
]