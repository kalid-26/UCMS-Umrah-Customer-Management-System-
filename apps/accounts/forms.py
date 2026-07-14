from django import forms
# from .models import CustomUser

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    