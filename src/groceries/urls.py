from django.contrib import admin
from django.urls import path, reverse, reverse_lazy

from .views import (
    grocery_inventory_view,
    grocery_insert_view,
    grocery_delete_view,
    grocery_detail_view,
    grocery_development_view,
    grocery_development_view0
)

urlpatterns = [
    path('', grocery_inventory_view, name="grocery-default-view"),
    path('inventory/', grocery_inventory_view, name="grocery-inventory"),
    path('insert/', grocery_insert_view, name="grocery-insert"),
    path('<int:id>/delete', grocery_delete_view, name="grocery-delete"),
    path('<int:id>/', grocery_detail_view, name="grocery-detail"),
    path('development', grocery_development_view, name="grocery-development"),
    path('development0', grocery_development_view0, name="grocery-development0")
]
