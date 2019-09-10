from django import forms
from .models import Signup


class SignUpForm(forms.Form):
    name = forms.CharField(
        max_length =60,
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Name"
        })
    )
    email = forms.EmailField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Email"
        })
    )
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
   

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Email"
        })
    )
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
   

