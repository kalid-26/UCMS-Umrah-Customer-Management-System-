from django import forms

from .models import Customer, Package, Payment

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "phone_number", "passport_number", "passport_expiry_date"]