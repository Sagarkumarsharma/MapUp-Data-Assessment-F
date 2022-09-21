from django.db import models
from django.contrib.auth.models import User #we are importing user model,which is take care of our user information
# Create your models here.

class Task(models.Model):  # model also known as database table
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):  #string representation of a model
        return self.title  #set the defualt value to the title

    #set the default ordering
    class Meta:
        ordering = ['complete']  #we wanna model ordered by complete status,any complete item should be send in bottom of the list
