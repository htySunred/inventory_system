# Author: lindafang
# Date: 7/8/24 10:29 AM
# File: forms.py
from django import forms
from dashboard.models import Product,Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']
