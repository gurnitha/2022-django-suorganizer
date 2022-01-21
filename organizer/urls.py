# organizer/urls.py

# Django modules
from django.conf.urls import url
from django.urls import path

from organizer.views import (
    StartupListView, StartupDetailView,
    TagListView, TagDetailView)

app_name = 'organizer'

urlpatterns = [
    path('startups/', StartupListView, name='startuplist'),
    path('startup/<str:slug>/', StartupDetailView, name='startupdetail'),
    path('tags/', TagListView, name='taglist'),
    path('tag/<str:slug>/', TagDetailView, name='tagdetail'),
]