"""grocerytracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from grocerytracker import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('success/', views.finished_registering, name='finished'),
    path('admin/', admin.site.urls),
    path('groceries/', include('groceries.urls')),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]

'''
    Example Flow path of a url 

    1. grocerytracker.urls (root) -> "path('groceries/', include('groceries.urls'))"
    2. -> groceries.urls -> "path('inventory/', grocery_inventory_view, name="grocery-inventory")"
    3. -> groceries.views -> Call on grocery_inventory_view() -> "return render(request, 'groceries/grocery_inventory.html', context)"
    4. -> templates/groceries -> grocery_inventory_update.html
    
'''
