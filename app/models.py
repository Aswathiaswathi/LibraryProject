from django.db import models

# Create your models here.
class library(models.Model):
   name = models.CharField(max_length=20)
   picture = models.ImageField()
   author = models.CharField(max_length=20)
   email = models.EmailField(blank=True)
   description = models.TextField()
   def __str__(self):
       return self.name