# blog/admin.py

# Django modules
from django.contrib import admin

# Locals
from blog.models import Post

# Register your models here.


admin.site.register(Post)
