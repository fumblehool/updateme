# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from random import choice
from string import letters
from forms import SignUpForm


def index(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            form.cleaned_data.get('choices')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/app/login')
    else:
        form = SignUpForm()
    return render(request, 'app/register.html', {'form': form})


def feedname(request, name):
    url = ""
    if name == "sports":
        url = "http://timesofindia.indiatimes.com/rssfeeds/4719148.cms?feedtype=json"
    elif name == "india":
        url = "http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms?feedtype=json"
    elif name == "science":
        url = "http://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms?feedtype=json"
    elif name == "environment":
        url = "http://timesofindia.indiatimes.com/rssfeeds/2647163.cms?feedtype=json"
    elif name == "tech":
        url = "http://timesofindia.indiatimes.com/rssfeeds/5880659.cms?feedtype=json"
    elif name == "entertainment":
        url = "http://timesofindia.indiatimes.com/rssfeeds/1081479906.cms?feedtype=json"
    req = requests.get(url)
    data = req.json()
    for i in data['channel']['item']:
        des = i['description']
        index = int(des.find('src='))
        if index is -1:
            img_src = "http://placehold.it/900x300"
        else:
            index = index + 5
            last = des.find('"', index)
            img_src = des[index: last]
        i['img'] = img_src

    return render(request, "app/feed.html", {'data': data}, {'title':name})

