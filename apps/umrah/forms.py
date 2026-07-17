from django import forms

from .models import Customer, UmrahApplication, Package, Payment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "phone_number", "passport_number", "passport_expiry_date"]
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = UmrahApplication
        fields = ["customer", "package", "status"]
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["application", "amount", "payment_method", "payment_date"]
        
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ["name", "price", "duration_days", "description"]