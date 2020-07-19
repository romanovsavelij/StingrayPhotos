from django.shortcuts import render
from uploader.models import Image
from django.http import HttpResponse
from http import HTTPStatus as Status
from django.core.exceptions import ValidationError
from utils import constants
from django.views.generic import View


class UploadView(View):
    def get(self, request, *args, **kwargs):
        persons_key = request.GET.get('key')
        if persons_key is None:
            return HttpResponse(constants.KEY_EXPECTED_MESSAGE, status=Status.BAD_REQUEST)

        return UploadView.get_home_page(request, persons_key)

    def post(self, request, *args, **kwargs):
        persons_key = request.GET.get('key')
        if persons_key is None:
            return HttpResponse(constants.KEY_EXPECTED_MESSAGE, status=Status.BAD_REQUEST)

        files = request.FILES.getlist('images')

        picture_ind = UploadView.get_first_adding_picture_ind(persons_key)
        for f in files:
            image = Image(persons_key=persons_key, picture=f, picture_ind=picture_ind)
            try:
                image.full_clean()
            except ValidationError:
                return HttpResponse(constants.FILE_SIZE_LIMIT_EXCEEDED_MESSAGE, status=Status.UNPROCESSABLE_ENTITY)
            else:
                image.save()
                picture_ind += 1

        return UploadView.get_home_page(request, persons_key)

    @staticmethod
    def put(request, *args, **kwargs):
        return HttpResponse(constants.INVALID_REQUEST_TYPE_MESSAGE, status=Status.METHOD_NOT_ALLOWED)

    @staticmethod
    def delete(request, *args, **kwargs):
        return HttpResponse(constants.INVALID_REQUEST_TYPE_MESSAGE, status=Status.METHOD_NOT_ALLOWED)

    @staticmethod
    def get_home_page(request, persons_key):
        images = list(Image.objects.filter(persons_key=persons_key))

        return render(request, 'home.html', {
            'images': images,
            'images_exist': bool(images),
        })

    @staticmethod
    def get_first_adding_picture_ind(persons_key):
        last_added_ind = 0
        while True:
            try:
                image = list(Image.objects.filter(persons_key=persons_key, picture_ind=last_added_ind))[0]
            except IndexError:
                return last_added_ind
            last_added_ind += 1
