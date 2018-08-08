from django.conf.urls import url

from . import views
from .views import OrderCreate,ListOrders,OrderUpdate


app_name = "orderform"

urlpatterns = [
    # # /orderform/
    # url(r'^$', views.orderform, name='index'),

    # /orderform/cakemonster
    url(r'^cakemonster/$', OrderCreate.as_view(), name='cakemonster'),

    # /orderform/listorders
    url(r'^listorders/$', ListOrders.as_view(), name='listorders'),

    url(r'^(?P<pk>[0-9]+)/update/$', OrderUpdate.as_view(), name="updateorder"),

]
