from django.shortcuts import render
from uploader.models import Image

main_picture_src = 0
persons_key = 0
picture_ind = 0

def home(request):
    print('In presenter!')
    global main_picture_src
    global persons_key
    global picture_ind
    if request.method == 'POST':
        print('next image')
        picture_ind += 1
    else:
        print('get page')
        persons_key = request.GET.get('key', 1111)
    # main_picture_src = '../media/images/background.png'
    try:
        image = Image.objects.get(id=int(f'{persons_key}{picture_ind}'))
    except Image.DoesNotExist:
        picture_ind = 0
        image = Image.objects.get(id=int(f'{persons_key}{picture_ind}'))

    main_picture_src = image.picture.url
    return render(request, 'presenter.html', {'main_picture_src': main_picture_src})

# Create your views here.
