from django.shortcuts import render
from django.views.static import serve
from uploader.models import Image
import os

picture_ind_by_key = {}

def home(request):
    persons_key = request.GET.get('key', 1111)
    if persons_key not in picture_ind_by_key:
        picture_ind_by_key.update({persons_key: 0})
    else:
        picture_ind_by_key[persons_key] += 1

    picture_ind = picture_ind_by_key[persons_key]
    # filepath = './media/images/bird.png'
    try:
        image = Image.objects.get(id=int(f'{persons_key}{picture_ind}'))
    except Image.DoesNotExist:
        picture_ind = 0
        image = Image.objects.get(id=int(f'{persons_key}{picture_ind}'))

    picture_src = '.' + image.picture.url
    print(f'picture_src: {picture_src}')
    return serve(request, os.path.basename(picture_src), os.path.dirname(picture_src))
