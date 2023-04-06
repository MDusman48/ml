from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

# Create your models here.
 
# class CustomUser(AbstractUser):
 
    
#     email = models.EmailField(unique=True)
    
#     def __str__(self):
#         return self.username

class SaveDocument(models.Model):
    name = models.CharField('name', max_length=150)
    gallery = models.ImageField(null=True, blank=True, upload_to="images/")
    document = models.ImageField(null=True, blank=True, upload_to="documents/")
    def __str__(self):
        return self.name



        

