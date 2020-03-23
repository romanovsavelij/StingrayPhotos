from django.db import models


class Image(models.Model):
    picture = models.FileField(upload_to='images/')
    persons_key = models.PositiveSmallIntegerField(default='1111')
    picture_ind = models.PositiveSmallIntegerField(default=0)
