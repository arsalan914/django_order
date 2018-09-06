from django.db import models
from django.shortcuts import render
# Create your models here.
from django.urls import reverse


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'documents/{0}/{1}_{2}/{3}'.format(instance.date, instance.fullname,instance.contactnumber, filename)

class Order(models.Model):
    STATUS_VALUES = (
        (-1, 'Rejected'),
        (0, 'Not-Accepted'),
        (1, 'Accepted'),
        (2, 'Ready-for-delivery'),
        (3, 'Completed'),
    )
    FLAVOR_VALUES = (
        (0, 'Chocolate Chip'),
        (1, 'Chocolate Fudge'),
        (2, 'Nutella'),
        (3, 'Cheese'),
        (4, 'Strawberry Cheese'),
    )
    fullname = models.CharField(max_length=300)
    contactnumber = models.BigIntegerField()
    date = models.DateField()
    time = models.TimeField()
    # flavor = models.CharField(max_length=300)
    flavor = models.IntegerField(default=0, choices=FLAVOR_VALUES)
    image1 = models.FileField(null=True,upload_to=user_directory_path)
    image2 = models.FileField(null=True,upload_to=user_directory_path)
    # image1 = models.FileField(null=True,upload_to='documents/%Y%m%d/')
    # image2 = models.FileField(null=True,upload_to='documents/%Y%m%d/')
    status = models.IntegerField(default=0, choices=STATUS_VALUES)

    def get_absolute_url(self):
        print ("get abosilte url")
        return "%s?posted=yes" % reverse('orderform:listorders')