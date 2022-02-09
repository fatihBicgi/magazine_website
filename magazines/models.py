from operator import truediv
from pydoc import describe
from unicodedata import category
from django.db import models

# Create your models here.

class Magazine(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    real_content = models.TextField(default="",)
    image =models.CharField(max_length=50)
    created_date =models.DateTimeField(auto_now_add=True)
    isPublished=models.BooleanField(default=True)

    

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/images/' + self.image
        

