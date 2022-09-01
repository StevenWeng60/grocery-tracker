from django import forms
from .models import Grocery
from .models import GroceryListItem


class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = [
            'name',
            'quantity',
            'store',
        ]

class GroceryListItemForm(forms.ModelForm):
    class Meta:
        model = GroceryListItem
        fields = [
            'name',
            'quantity',
        ]

class UpdateForm(forms.Form):
    quantity = forms.IntegerField()