# organizer/models.py

# Django modules
from django.db import models
from django.urls import reverse

# Locals

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31,unique=True,help_text='A label for URL config.')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_tag_absolute_url(self):
        return reverse('organizer:tagdetail', 
                        kwargs={'slug':self.slug})



class Startup(models.Model):
    name 			= models.CharField(max_length=31, db_index=True)
    slug 			= models.SlugField(max_length=31,unique=True,help_text='A label for URL config.')
    description 	= models.TextField()
    founded_date 	= models.DateField('date founded')
    contact 		= models.EmailField()
    website 		= models.URLField(max_length=255)
    tags 			= models.ManyToManyField(Tag)

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

    def __str__(self):
        return self.name

    def get_startup_absolute_url(self):
        return reverse('organizer:startupdetail', 
                        kwargs={'slug':self.slug})

class NewsLink(models.Model):
    title 		= models.CharField(max_length=63)
    pub_date 	= models.DateField('date published')
    link 		= models.URLField(max_length=255)
    startup 	= models.ForeignKey(Startup, on_delete=models.CASCADE)

    class Meta:
        verbose_name 	= 'news article'
        ordering 		= ['-pub_date']
        get_latest_by 	= 'pub_date'

    def __str__(self):
        return "{}: {}".format(
            self.startup, self.title)