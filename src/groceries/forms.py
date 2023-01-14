from django import forms
from .models import Grocery
from .models import GroceryListItem
from django.contrib.auth.models import User


class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = [
            'name',
            'quantity',
            'store',
        ]

    def save(self, user, commit=True):
        Grocery = super(GroceryForm, self).save(commit=False)
        Grocery.username = user
        if commit:
            Grocery.save()
        return Grocery


class GroceryListItemForm(forms.ModelForm):
    class Meta:
        model = GroceryListItem
        fields = [
            'name',
            'quantity',
        ]

    def save(self, user, commit=True):
        GroceryListItem = super(GroceryListItemForm, self).save(commit=False)
        GroceryListItem.username = user
        if commit:
            GroceryListItem.save()
        return GroceryListItem


class UpdateForm(forms.Form):
    quantity = forms.IntegerField()
