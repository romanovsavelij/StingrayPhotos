from django.http import HttpResponse
from uploader.models import Image

picture_ind_by_key = {}


def home(request):
    persons_key = request.GET.get('key', 1111)
    if persons_key not in picture_ind_by_key:
        picture_ind_by_key.update({persons_key: 0})
    else:
        picture_ind_by_key[persons_key] += 1

    picture_ind = picture_ind_by_key[persons_key]

    images = list(Image.objects.filter(persons_key=persons_key, picture_ind=picture_ind))
    if len(images) == 0:
        picture_ind_by_key[persons_key] = 0

        first_images = list(Image.objects.filter(persons_key=persons_key, picture_ind=0))
        if len(first_images) == 0:
            picture_src = './static/FileNotFound.png'
        else:
            image = first_images[0]
            picture_src = '.' + image.picture.url
    else:
        image = images[0]
        picture_src = '.' + image.picture.url

    with open(picture_src, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
