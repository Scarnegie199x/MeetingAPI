from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    title_choices = [
        ('employee', 'Employee'),
        ('supervisor', 'Supervisor'),
        ('manager', 'Manager'),
        ('director', 'Director'),
    ]
    title = models.CharField(max_length=20, choices=title_choices)

