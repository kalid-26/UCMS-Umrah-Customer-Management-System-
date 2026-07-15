from django.db import models
from django.conf import settings

# Create your models here.

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True, editable=False)
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    
    passport_number = models.CharField(max_length=50, unique=True)
    passport_expiry_date = models.DateField()
    
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.customer_id} - {self.first_name} {self.last_name}"