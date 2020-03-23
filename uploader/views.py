from django.shortcuts import render
# from uploader.models import UploadForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from uploader.models import Image

persons_key = 0


def home(request):
    global persons_key
    if request.method == 'GET':
        persons_key = request.GET.get('key', 1111)
    else:
        # saving loaded pictures
        files = request.FILES.getlist('images')
        picture_ind = 0
        for f in files:
            image = Image(persons_key=persons_key, picture=f, picture_ind=picture_ind)
            image.save()
            picture_ind += 1

    # getting images with such a persons_key
    images = list(Image.objects.filter(persons_key=persons_key))

    return render(request, 'home.html', {
        'images': images,
        'images_bool': bool(images),
        'not_img_bool': not bool(images),
    })