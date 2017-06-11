from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,)
    OPTIONS = (
                ("Sp", "Sports"),
                ("Mo", "Movies"),
                ("Tr", "Travels"),
                )
    # choices = forms.MultipleChoiceField(widget=forms.MultiValueField,)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )