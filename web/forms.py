from django.forms import ModelForm
from .models import Feeddback, Order


class FeedbackForm(ModelForm):
    class Meta:
        model = Feeddback
        fields = ['customer_first_name', 'customer_second_name', 
                  'feedback_description', 'feedback', 'customer_photo', 'deleted']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer_first_name', 'customer_second_name', 'country', 'town', 'address',
                  'postalcode',  'order_description', 'order', 'customer_photo', 'deleted']
