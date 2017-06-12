# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from forms import SignUpForm


# Static url for fetching news data.
static_url = "http://timesofindia.indiatimes.com/rssfeeds/"

# Mapper maps string names to api endpoints.
mapper = {
    "sports": "4719148.cms?feedtype=json",
    "india": "-2128936835.cms?feedtype=json",
    "science": "-2128672765.cms?feedtype=json",
    "environment": "2647163.cms?feedtype=json",
    "tech": "5880659.cms?feedtype=json",
    "entertainment": "1081479906.cms?feedtype=json"
}


def index(request):  # index
    return render(request, 'app/index.html')


def register(request):  # Register handler
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            form.cleaned_data.get('choices')
            raw_password = form.cleaned_data.get('password1')
            # category = form.cleaned_data.get('category')
            form.save()
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/app/login')
    else:
        form = SignUpForm()
    return render(request, 'app/register.html', {'form': form})


def feedname(request, name):  # News feed generator
    if request.user.is_authenticated:
        if name in mapper:
            url = static_url + mapper[name]
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
            return render(request, "app/feed.html",
                          {'data': data}, {'title': name})
        else:
            return render(request, "app/404.html")
    else:
        return redirect("/app/login")
