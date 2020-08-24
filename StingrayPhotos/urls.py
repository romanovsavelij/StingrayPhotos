"""StingrayPhotos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from uploader import views as uploader_views
from auth import views as auth_views
from get_key import views as get_key_views
from get_image import views as get_image_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', uploader_views.UploadView.as_view(), name='image_upload'),
    path('', auth_views.auth, name='auth_index'),
    path('get_key/', get_key_views.home, name='get_key'),
    path('get_image/', get_image_views.home, name='get_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
