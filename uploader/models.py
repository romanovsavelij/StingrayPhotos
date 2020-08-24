from django.db import models
from django.core.exceptions import ValidationError
from utils.memory import TEN_MEGABYTES_IN_BYTES


def validate_file_size(value):
    if value.size > TEN_MEGABYTES_IN_BYTES:
        raise ValidationError(f'The maximum file size that can be '
                              f'uploaded is {TEN_MEGABYTES_IN_BYTES} bytes')
    else:
        return value


class Image(models.Model):
    picture = models.FileField(upload_to='images/',
                               validators=[validate_file_size])
    persons_key = models.PositiveSmallIntegerField(default='1111')
    picture_ind = models.PositiveSmallIntegerField(default=0)
