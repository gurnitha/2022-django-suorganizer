# blog/urls.py

# Django modules
from django.conf.urls import url
from django.urls import path

from blog.views import greeting

app_name = 'blog'

urlpatterns = [
    # url(r'^$', greeting),
    # path('', greeting, name='greeting'),
]