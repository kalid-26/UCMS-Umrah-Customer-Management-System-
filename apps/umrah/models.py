from django.db import models
from django.conf import settings
from .chioces import ApplicationStatus, PaymentMethod


from datetime import datetime
# Create your models here.

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True, editable=False)
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    
    passport_number = models.CharField(max_length=50, unique=True)
    passport_expiry_date = models.DateField()
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.customer_id:
            current_year = datetime.now().year
            prefix = f"UMR-{current_year}"
            
            last_customer = Customer.objects.filter(
                customer_id__startswith=prefix
            ).order_by('-customer_id').first()
            
            if last_customer:
                last_number = int(last_customer.customer_id.split("-")[-1])
                new_number = last_number + 1
                
            else:
                new_number = 1
                
            self.customer_id = (f"{prefix}-{new_number:04d}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.customer_id} - {self.first_name} {self.last_name}"
    
class Package(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return f"{self.name} {self.price}"
    
class UmrahApplication(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="applications")
    package = models.ForeignKey(Package, on_delete=models.PROTECT)
    status = models.CharField(max_length=200, choices=ApplicationStatus.choices, default=ApplicationStatus.PENDING)
    registration_date = models.DateField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.customer.customer_id}-{self.package.name}"
    
class Payment(models.Model):
    application = models.ForeignKey(UmrahApplication, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    payment_date = models.DateField()
    reference_number = models.CharField(max_length=100, blank=True)
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.application.customer.customer_id}-{self.amount}"