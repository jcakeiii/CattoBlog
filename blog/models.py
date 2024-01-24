from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model): #each class is its own table in the database
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) #set the date posted to current date   
    author = models.ForeignKey(User, on_delete=models.CASCADE) #pass in the related User table and what we want Django to do if the user who created the post gets deleted: if a user gets deleted, delete the post 
    #redirect vs reverse:will return the full url to that route as a string

    def __str__(self): #dunder method???
        return self.title
    
    def get_absolute_url(self): 
        return reverse('post-detail', kwargs={'pk': self.pk})