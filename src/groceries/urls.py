from django.contrib import admin
from django.urls import path, reverse, reverse_lazy

from .views import (
    grocery_inventory_view,
    grocery_insert_view,
    grocery_delete_view,
    grocery_detail_view,
    grocery_development_view,
    grocery_development_view0,
    grocery_modify_view,
    grocery_change_view
)

urlpatterns = [
    path('', grocery_inventory_view, name="grocery-default-view"),
    path('inventory/', grocery_inventory_view, name="grocery-inventory"),
    path('modify/', grocery_modify_view, name="grocery-modify"),
    path('modify/insert/', grocery_insert_view, name="grocery-insert"),
    path('modify/delete/', grocery_delete_view, name="grocery-delete"),
    path('modify/change/', grocery_change_view, name="grocery-change"),
    path('<int:id>/', grocery_detail_view, name="grocery-detail"),
    path('development', grocery_development_view, name="grocery-development"),
    path('development0', grocery_development_view0, name="grocery-development0")
]
