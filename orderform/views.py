from django.shortcuts import render
import pyrebase
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import  Order
from django import forms
from django.views import generic
from django.contrib.admin import widgets
import datetime

# def orderform(request):
#     return render(request, 'orderform.html')

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['date'].label = "Delivery Date"
        self.fields['time'].label = "Delivery Time"
        self.fields['date'].widget.input_type = "date"
        self.fields['time'].widget.input_type = "time"
        self.fields['contactnumber'].widget.input_type = "text"
        # print (self.fields.values())
        # print (self.fields)
        for field in self.fields.values():
            # print (field.label)
            if field.label == 'Contactnumber':
                field.widget.attrs = {'class': 'form-control', 'placeholder': '0321-1234567', 'pattern' : '[0-9]{4}-[0-9]{7}'}
            elif field.label == 'Delivery Date':
                # field.widget.attrs = {'class': 'form-control', 'onchange': 'checkdate()'}
                field.widget.attrs = {'class': 'form-control'}
            else:
                field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Order
        # fields = "__all__"
        fields = ['fullname','date','time', 'contactnumber', 'flavor', 'image1', 'image2']

class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm

    # no need for this function but let it be
    def form_valid(self, form):
        obj = form.save(commit=False)
        return super(OrderCreate, self).form_valid(form)

class OrderUpdate(UpdateView):
    form_class = OrderForm
    model = Order

class StatusUpdate(UpdateView):
    model = Order
    fields = ['status']
    success_url = reverse_lazy('orderform:listorders')
    template_name = "orderform/statusupdate_form.html"


    def get_success_url(self):
        # can be used to presever query parameters
        print (len(self.request.GET))
        return self.success_url

class ListOrders(generic.ListView):
    template_name = "orderform/orders.html"
    context_object_name = 'all_orders'

    def get_queryset(self):
        start_date = self.request.GET.get('startdate')
        end_date = self.request.GET.get('enddate')
        # if self.request.user.is_authenticated():
        if (start_date != "" and start_date != None and end_date != None and end_date!=""):
            print ("\r\n\r\n\r\n\r\n\r\n")
            print (start_date)
            print (end_date)
            return Order.objects.filter(date__range=[start_date, end_date]).order_by('-date','time')

        #current date
        # (datetime.datetime.now().date())

        return Order.objects.all().order_by('-date','time')
        # else:
        #     return None


def cakemonster(request):
     return render(request, 'orderform/cakemonster.html')
