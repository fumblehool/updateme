# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login as auth_login, authenticate

from forms import SignUpForm


def index(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            form.cleaned_data.get('choices')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'app/register.html', {'form': form})


def feed(request, page_number):
    url = "https://newsapi.org/v1/articles?source=techcrunch&apiKey="
    apiKey = "4a77eea012f040af80f1afdd10d7be55"
    u = "http://timesofindia.indiatimes.com/rssfeeds/-2128838597.cms?feedtype=sjson"
    r = requests.get(u)
    data = r.json()
    data = data['channel']
    return render(request, "app/feed.html", {'data': data})
