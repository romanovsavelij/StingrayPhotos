# Generated by Django 3.0.4 on 2020-03-23 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20200323_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]
