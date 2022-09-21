from time import timezone
from django.db import models
from django.utils import timezone
#import the user model
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Date_Posted = models.DateTimeField(default = timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


    #get absolute url to tell django how to find the url of any specific instance of a post
    def get_absolute_url(self):
        return reverse('post1-detail', kwargs={'pk': self.pk}) 
    
