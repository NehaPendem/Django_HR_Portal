from django import forms
from django.contrib.auth import get_user_model
from .validators import validate


class SignupForm(forms.ModelForm):
    """user signup form"""
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate])

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'name', 'password',)


class LoginForm(forms.Form):
    """user login form"""
    id = forms.IntegerField()

    password = forms.CharField(widget=forms.PasswordInput())
