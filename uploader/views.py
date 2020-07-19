from django.shortcuts import render
from uploader.models import Image

# persons_key = 0


def home(request):
    # global persons_key
    persons_key = request.GET.get('key', 1111)
    if request.method == 'GET':
        print('in get request')

        # persons_key = request.GET.get('key', 1111)
    else:
        print('in post request')
        print(f'saving with person_key: {persons_key}')

        # Saving loaded pictures
        files = request.FILES.getlist('images')

        picture_ind = 0
        for f in files:
            image = Image(persons_key=persons_key, picture=f, picture_ind=picture_ind)
            image.save()
            picture_ind += 1

    print(f'get images with persons_key {persons_key}')

    images = list(Image.objects.filter(persons_key=persons_key))

    print(f'images: {images}')

    return render(request, 'home.html', {
        'images': images,
        'images_exist': bool(images),
    })
