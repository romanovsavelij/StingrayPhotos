import random
import time
from django.http import JsonResponse

MIN_KEY = 1000
MAX_KEY = 9999


def home(request):
    random.seed(time.time())
    key = random.randint(MIN_KEY, MAX_KEY)
    return JsonResponse({'key': key})
