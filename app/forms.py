from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    OPTIONS = (
                ("Sp", "Sports"),
                ("Mo", "Movies"),
                ("Tr", "Travels"),
                ("Po", "Politics"),
                )
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)
    class Meta:
        model = User
        fields = ('email', 'choices', 'password1', 'password2', )