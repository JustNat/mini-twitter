from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

class Post(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    label = models.CharField(max_length=255)
