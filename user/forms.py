from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class register_users(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    briday_Date = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))


class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'briday_Date', 'password1', 'password2',)



