from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models


# Creating the post model 
class Post(models.Model):
    title= models.CharField(max_length=200)
    text= TextField()
    author = modelS.Foreignkey(settings.AUTH_USER_MODEL, o_delete=models.CASCADE)
    Created_date = models.DateTimeField(default=timezone.now)
    Published_date = models.DateTimeField(blank = True, null=True)