from django.http import HttpResponse
from django.shortcuts import render
from django.views.static import serve
from uploader.models import Image
from django.shortcuts import render
import os

picture_ind_by_key = {}

def home(request):
    persons_key = request.GET.get('key', 1111)
    print(f'picture_ind_by_key: {picture_ind_by_key}')
    if persons_key not in picture_ind_by_key:
        print(f'no key {persons_key} found')
        picture_ind_by_key.update({persons_key: 0})
    else:
        picture_ind_by_key[persons_key] += 1

    picture_ind = picture_ind_by_key[persons_key]
    # filepath = './media/images/bird.png'

    try:
        try:
            image = Image.objects.get(id=int(f'{persons_key}{picture_ind}'))
        except Image.DoesNotExist:
            picture_ind = 0
            picture_ind_by_key[persons_key] = 0
            image = Image.objects.get(id=int(f'{persons_key}{picture_ind}'))
        picture_src = '.' + image.picture.url
    except Image.DoesNotExist:
        picture_src = './media/images/fire.png'

    print(f'picture_src: {picture_src}')
    # return serve(request, os.path.basename(picture_src), os.path.dirname(picture_src))

    with open(picture_src, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
    # return render(request, 'bird.png')
