from django.db import models

# Create your models here.
from django.db import models


# Creating the post model 
class Post(models.Model):
    title: models.CharField(max_length=200)
    text: TextField()
    