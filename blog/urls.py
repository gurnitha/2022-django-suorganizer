# blog/urls.py

# Django modules
from django.conf.urls import url
from django.urls import path

from blog.views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    # url(r'^$', greeting),
    path('', PostListView, name='postlist'),
    path('<int:year>/<int:month>/<str:slug>/', PostDetailView, name='postdetail'),
]