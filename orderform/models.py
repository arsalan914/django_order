from django.db import models
from django.shortcuts import render
# Create your models here.
from django.urls import reverse


class Order(models.Model):
    STATUS_VALUES = (
        (-1, 'Rejected'),
        (0, 'Not-Accepted'),
        (1, 'Accepted'),
        (2, 'Ready-for-delivery'),
        (3, 'Completed'),
    )
    fullname = models.CharField(max_length=300)
    contactnumber = models.BigIntegerField()
    date = models.DateField()
    time = models.TimeField()
    flavor = models.CharField(max_length=300)
    image1 = models.FileField(null=True,upload_to='documents/%Y%m%d/')
    image2 = models.FileField(null=True,upload_to='documents/%Y%m%d/')
    status = models.IntegerField(default=0, choices=STATUS_VALUES)

    def get_absolute_url(self):
        print ("get abosilte url")
        return "%s?posted=yes" % reverse('orderform:listorders')

