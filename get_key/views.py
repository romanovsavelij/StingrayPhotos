import random
import time
from django.http import JsonResponse
from typing import Final

MIN_KEY: Final = 1000
MAX_KEY: Final = 9999


def home(request):
    random.seed(time.time())
    key = random.randint(MIN_KEY, MAX_KEY)
    return JsonResponse({'key': key})
