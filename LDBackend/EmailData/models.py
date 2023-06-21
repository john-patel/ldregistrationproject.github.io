from django.db import models
# import uuid


class RegisterData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    confirmpassword = models.CharField(max_length=10)