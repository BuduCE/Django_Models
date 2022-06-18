from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models


# Creating the post model 
class Post(models.Model):
    title= models.CharField(max_length=200)
    text= TextField()
    author = model.Foreignkey(settings.AUTH_USER_MODEL)
    Created_date = models.DateTimeField(defau)