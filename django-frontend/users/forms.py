from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=120, help_text='Required. Enter a valid email address.')
    website_link = forms.CharField(max_length=50, required=False, help_text='Optional.')
    social_media_link = forms.CharField(max_length=50, required=False, help_text='Optional.')
    gender = forms.CharField(max_length=50, required=False, help_text='Optional.')
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','website_link', 'social_media_link','password2','gender','photo')