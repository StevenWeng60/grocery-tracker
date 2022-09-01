from django.contrib import admin
from django.urls import path, reverse, reverse_lazy

from .views import (
    grocery_inventory_view,
    grocery_insert_view,
    grocery_delete_overview,
    grocery_delete_object_view,
    grocery_detail_view,
    grocery_development_view,
    grocery_development_view0,
    grocery_modify_view,
    grocery_update_overview,
    grocery_update_object_view,
    grocery_list_overview,
    grocery_list_settings_view,
)

urlpatterns = [
    path('', grocery_inventory_view, name="grocery-default-view"),
    path('inventory/', grocery_inventory_view, name="grocery-inventory"),
    path('modify/', grocery_modify_view, name="grocery-modify"),
    path('modify/insert/', grocery_insert_view, name="grocery-insert"),
    path('modify/delete/', grocery_delete_overview, name="grocery-delete-overview"),
    path('modify/delete/<int:id>/', grocery_delete_object_view, name="grocery-delete-object-view"),
    path('modify/update/', grocery_update_overview, name="grocery-update-overview"),
    path('modify/update/<int:id>/', grocery_update_object_view, name="grocery-update-object-view"),
    path('<int:id>/', grocery_detail_view, name="grocery-detail"),
    path('development', grocery_development_view, name="grocery-development"),
    path('development0', grocery_development_view0, name="grocery-development0"),
    path('grocery_list/', grocery_list_overview, name="grocery-list-overview"),
    path('grocery_list/settings', grocery_list_settings_view, name="grocery-list-settings-view"),
]
