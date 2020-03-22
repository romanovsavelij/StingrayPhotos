from django.db import models
from django.forms import ModelForm
from django import forms


class Image(models.Model):
    name = models.CharField(max_length=500)
    picture = models.FileField(upload_to='images/')