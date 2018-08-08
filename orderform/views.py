from django.shortcuts import render
import pyrebase

# Create your views here.
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import  Order

from django import forms
from django.views import generic

from django.contrib.admin import widgets


# def orderform(request):
#     return render(request, 'orderform.html')


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.input_type = "date"
        self.fields['time'].widget.input_type = "time"
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Order
        fields = "__all__"

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

        return Order.objects.all().order_by('-date','time')
        # else:
        #     return None
