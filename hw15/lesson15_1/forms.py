from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime


class FirstForm(forms.Form):
    quantity = forms.IntegerField()
    product = forms.CharField()
    # order_date = forms.DateField()

    def clean_quantity(self):
        print('ckean quantity')
        print(datetime.now().date())
        quantity = self.cleaned_data['quantity']
        if quantity > 100:
            print('more then 100')
            raise ValidationError('too big')
        return quantity

    # def clean_order_date(self):
    #     order_date = self.cleaned_data['order_date']
    #     print('проверка')
    #     if order_date < datetime.now().date():
    #         raise ValidationError('date_date')
    #     return order_date

    def clean(self):
        print('Cleaning self')
        return self.cleaned_data

