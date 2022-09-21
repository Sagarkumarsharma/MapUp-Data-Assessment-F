from django.contrib import admin

# Register your models here.
from .models import Task #importing our model

admin.site.register(Task)