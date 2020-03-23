from django.http import HttpResponse
from django.shortcuts import render
from django.views.static import serve
from uploader.models import Image
from django.shortcuts import render
import os

picture_ind_by_key = {}


def home(request):
    persons_key = request.GET.get('key', 1111)
    if persons_key not in picture_ind_by_key:
        picture_ind_by_key.update({persons_key: 0})
    else:
        picture_ind_by_key[persons_key] += 1

    picture_ind = picture_ind_by_key[persons_key]

    try:
        try:
            image = list(Image.objects.filter(persons_key=persons_key, picture_ind=picture_ind))[0]
        except IndexError:
            # collection of images ended
            picture_ind = 0
            picture_ind_by_key[persons_key] = 0
            image = list(Image.objects.filter(persons_key=persons_key, picture_ind=picture_ind))[0]
        picture_src = '.' + image.picture.url
    except IndexError:
        # there are no images with such a persons_key
        picture_src = './media/images/fire.png'

    with open(picture_src, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")