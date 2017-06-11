# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == "POST":
        return HttpResponse("POSTED")
    return render(request, "app/register.html")


def login(request):
    return render(request, "app/login.html")


def feed(request, page_number):
    return render(request, "app/feed.html", {'number':page_number})
