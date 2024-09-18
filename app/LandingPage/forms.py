from django import forms

class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Product Name')
    category = forms.CharField(required=False, label='Category')
    min_price = forms.DecimalField(required=False, label='Min Price', min_value=0)
    max_price = forms.DecimalField(required=False, label='Max Price', min_value=0)
