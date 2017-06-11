# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})


def feed(request, page_number):
    return render(request, "app/feed.html", {'number':page_number})
