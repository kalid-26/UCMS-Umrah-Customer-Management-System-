import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import (
    Customer, 
    UmrahApplication, 
    Package, 
    Payment
)

def validate_phone_number(value):
    pattern = r"^\+[1-9]\d{7,14}$"    
    
    if not re.match(pattern, value):
        raise ValidationError(
            "Enter a valid international phone number. Example: +251911123456"
        )

class BootstrapForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "form-control"
                }
            )

class CustomerForm(BootstrapForMixin, forms.ModelForm):
    
    phone_number = forms.CharField(
        validators=[validate_phone_number]
    )
    
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "phone_number", "passport_number", "passport_expiry_date"]
        
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Abel"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Meka"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "example@gmail.com"
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "+251911121314"
                }
            ),
            "passport_number": forms.TextInput(
                attrs={
                }
            ),
            "passport_expiry_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }
        
    def clean_passport_expiry_date(self):
        expiry_date = self.cleaned_data.get("passport_expiry_date")
        
        if expiry_date <= timezone.now().date():
            raise ValidationError("Passport Expiry date must be a future date.")
        return expiry_date
    
class ApplicationForm(BootstrapForMixin, forms.ModelForm):
    
    class Meta:
        model = UmrahApplication
        fields = ["customer", "package", "status"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["customer"].queryset = (
            Customer.objects.filter(is_active=True)
        )

        self.fields["package"].queryset = (
            Package.objects.filter(is_active=True)
        )
class PaymentForm(BootstrapForMixin, forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["application", "amount", "payment_method", "payment_date"]
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["application"].queryset = (
            UmrahApplication.objects.filter(is_active=True)
        )
    
    def clean_payment_date(self):
        payment_date = self.cleaned_data.get("payment_date")
        
        if payment_date and payment_date > timezone.now().date():
            raise ValidationError(
                "Payment must be paid today not for future."
            )
            
        return payment_date
    
    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        
        if amount is not None and amount <= 0:
            raise ValidationError(
                "Payment amount must be greater than zero."
            )
        
        return amount
    
class PackageForm(BootstrapForMixin, forms.ModelForm):
    class Meta:
        model = Package
        fields = ["name", "price", "duration_days", "description"]
        
    def clean_price(self):
        price = self.cleaned_data.get("price")
        
        if price is not None and price <= 0:
            raise ValidationError(
                "Price must be greater than zero."
            )
        return price
    
    def clean_duration_days(self):
        duration_days = self.cleaned_data.get("duration_days")
        
        if duration_days is not None and duration_days <= 0:
            raise ValidationError(
                "Duration must be at least 1 day."
            )
        return duration_days