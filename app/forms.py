from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,)
    OPTIONS = (
              ("sports", "Sports"),
              ("entertainment", "Entertainment"),
              ("tech", "Technology"),
              ("environment", "Environment"),
              ("science", "Science")
    )
    category = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'category')
