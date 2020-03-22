from django.shortcuts import render
# from uploader.models import UploadForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from uploader.models import Image

persons_key = 0

def home(request):
    global persons_key
    # print(f'person_key: {persons_key}')
    if request.method == 'GET':
        persons_key = request.GET.get('key', 1111)
        # image = Image.objects.get(id=int(f'{persons_key}{picture_ind}'))
    else:
        files = request.FILES.getlist('images')
        # print(f'{len(files)} files loaded!')
        picture_ind = 0
        for f in files:
            # print(f'picture_ind: {picture_ind}')
            image = Image(id=int(f'{persons_key}{picture_ind}'), picture=f)
            image.save()
            picture_ind += 1
    return render(request, 'home.html')