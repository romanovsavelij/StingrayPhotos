from django.shortcuts import render
import random
import time
from django.http import JsonResponse

def home(request):
    random.seed(time.time())
    key = random.randint(1000, 9999)
    return JsonResponse({'key': key})

# Create your views here.
