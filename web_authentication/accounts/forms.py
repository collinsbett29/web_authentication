from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    profile_pic = forms.ImageField() 
    ROLE_CHOICES =(
        ("1", "Admin"),
        ("2", "User"),
        )
    role = forms.ChoiceField(choices= ROLE_CHOICES)



    class Meta:
        model = User
        fields = ["username", "email", "profile_pic", "phone_number", "password1", "password2", "role"]
