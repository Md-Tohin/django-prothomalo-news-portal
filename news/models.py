from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class News(models.Model):
    news_title      = models.CharField(max_length=250, unique=True)
    slug            = models.SlugField(max_length=300, unique=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail          = models.ImageField(upload_to='photos/news/thumbnail')
    images          = models.ImageField(upload_to='photos/news/')
    short_description     = models.TextField(max_length=500, blank=True)
    long_description     = models.TextField(blank=True)   
    meta_title     = models.TextField(max_length=500, blank=True)
    meta_description     = models.TextField(blank=True)
    meta_keyword     = models.TextField(max_length=500, blank=True)
    is_read    = models.BooleanField(default=False)
    is_discussed    = models.BooleanField(default=False)
    is_selected    = models.BooleanField(default=False)
    is_image   = models.BooleanField(default=False)
    is_top    = models.BooleanField(default=False)
    is_publish    = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('news_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.news_title