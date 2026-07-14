from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    STAFF = 'STAFF', 'Staff'

class CustomUser(AbstractUser):
    role = models.CharField(max_length=15, choices=UserRole.choices, default=UserRole.STAFF)