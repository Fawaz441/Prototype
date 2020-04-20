from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

class Offer(models.Model):
    client_name = models.CharField(max_length=30)
    service = models.CharField(max_length=40)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True,blank=True)
    image = models.ImageField(upload_to='media/',blank=True,null=True)
    author = models.ForeignKey('auth.User',related_name='posts',on_delete=models.CASCADE)
    area = models.CharField(max_length=20)
    slug = models.SlugField()

    def detail(self):
        return reverse('detail',kwargs={'slug':self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title,allow_unicode=True)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    



