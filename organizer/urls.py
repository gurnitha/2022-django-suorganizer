# organizer/urls.py

# Django modules
from django.conf.urls import url
from django.urls import path

from organizer.views import HomePageView, TagListView

app_name = 'organizer'

urlpatterns = [
    path('', HomePageView, name='homepage'),
    path('tags/', TagListView, name='taglist'),
]