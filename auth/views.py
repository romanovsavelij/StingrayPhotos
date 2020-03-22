from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def auth(request):
    return render(request, 'auth.html', dict())