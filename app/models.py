# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms


class User(models.Model):
    email = models.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class Category(models.Model):
    c_id = models.IntegerField()
    category_text = models.CharField(max_length=100, default="null")


class Mapper(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    c_id = models.IntegerField()

