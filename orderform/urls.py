from django.conf.urls import url

from . import views
from .views import *


app_name = "orderform"


urlpatterns = [
    # # /orderform/
    # url(r'^$', views.orderform, name='index'),

    # /orderform/cakemonster
    url(r'^cakemonster/$', OrderCreate.as_view(), name='cakemonster'),

    # /orderform/listorders
    url(r'^listorders/$', ListOrders.as_view(), name='listorders'),

    # /orderform/cakemonsterview
    url(r'^cakemonsterview/$', views.cakemonster, name='cakemonsterview'),

    # /orderform/2/update
    url(r'^(?P<pk>[0-9]+)/update/$', OrderUpdate.as_view(), name="updateorder"),

    # /orderform/2/statusupdate
    url(r'^(?P<pk>[0-9]+)/statusupdate/$', StatusUpdate.as_view(), name="statusupdate"),

    # /orderform/datatables
    url(r'^datatables/$', ListOrders2.as_view(), name="datatables"),

]
