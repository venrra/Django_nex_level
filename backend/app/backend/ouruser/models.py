from django.db import models


class User(models.Model):
    username = models.CharField(verbose_name="Username", max_length=32, unique=True)
    email = models.EmailField(verbose_name="User email", max_length=512)
    password = models.CharField(verbose_name="Password", max_length=32)
    name = models.CharField(verbose_name="User name", max_length=32)
    surname = models.CharField(verbose_name="User surname", max_length=32)
    
