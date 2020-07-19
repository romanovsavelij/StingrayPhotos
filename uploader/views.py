from django.shortcuts import render
from uploader.models import Image
from django.http import HttpResponse
from http import HTTPStatus as Status
from django.core.exceptions import ValidationError
from utils import constants


def home(request):
    persons_key = request.GET.get('key')
    if persons_key is None:
        return HttpResponse(constants.KEY_EXPECTED_MESSAGE, status=Status.BAD_REQUEST)

    if request.method == 'POST':
        files = request.FILES.getlist('images')

        picture_ind = 0
        for f in files:
            image = Image(persons_key=persons_key, picture=f, picture_ind=picture_ind)
            try:
                image.full_clean()
            except ValidationError:
                return HttpResponse(constants.FILE_SIZE_LIMIT_EXCEEDED_MESSAGE, status=Status.UNPROCESSABLE_ENTITY)
            else:
                image.save()
                picture_ind += 1
    elif request.method != 'GET':
        return HttpResponse(constants.INVALID_REQUEST_TYPE_MESSAGE, status=Status.BAD_REQUEST)

    images = list(Image.objects.filter(persons_key=persons_key))

    return render(request, 'home.html', {
        'images': images,
        'images_exist': bool(images),
    })
