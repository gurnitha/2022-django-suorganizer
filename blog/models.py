# blog/models.py

# Django modules
from django.db import models
from django.urls import reverse

# Locals
from organizer.models import Startup, Tag

# Create your models here.

class Post(models.Model):
    title 		= models.CharField(max_length=63)
    slug 		= models.SlugField(max_length=63,help_text='A label for URL config',unique_for_month='pub_date')
    text 		= models.TextField()
    pub_date 	= models.DateField('date published',auto_now_add=True)
    tags 		= models.ManyToManyField(Tag, related_name='blog_posts')
    startups 	= models.ManyToManyField(Startup, related_name='blog_posts')

    class Meta:
        verbose_name 	= 'blog post'
        ordering 		= ['-pub_date', 'title']
        get_latest_by 	= 'pub_date'

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))

    def get_post_absolute_url(self):
        return reverse('blog:postdetail',
                        args=[
                            self.pub_date.year,
                            self.pub_date.month,
                            self.pub_date.day,
                            self.slug
                        ])

