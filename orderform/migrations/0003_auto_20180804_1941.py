# Generated by Django 2.0.7 on 2018-08-04 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderform', '0002_auto_20180804_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='image2',
        ),
    ]
