from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import GroceryForm, GroceryListItemForm, UpdateForm
from .models import Grocery, GroceryListItem

# Create your views here.


def grocery_inventory_view(request):
    queryset = Grocery.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, 'groceries/grocery_inventory.html', context)


# LIST OF INVENTORY TAB VIEWS ----------------------------------------------------------------------
def grocery_modify_view(request):
    form = GroceryForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = GroceryForm()

    queryset = Grocery.objects.all()
    context = {
        'form': form,
        "object_list": queryset
    }

    return render(request, 'groceries/grocery_modify.html', context)


def grocery_insert_view(request):
    form = GroceryForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = GroceryForm()

    queryset = Grocery.objects.all()
    context = {
        'form': form,
        "object_list": queryset
    }

    return render(request, 'groceries/grocery_insert.html', context)


def grocery_delete_object_view(request, id):
    obj = get_object_or_404(Grocery, id=id)

    if request.method == "POST":
        print("POST")
        obj.delete()
        return redirect('../')

    queryset = Grocery.objects.all()

    context = {
        "object": obj,
        "object_list": queryset
    }
    return render(request, "groceries/grocery_delete.html", context)


def grocery_update_object_view(request, id):
    obj = get_object_or_404(Grocery, id=id)

    form = UpdateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            grocery = Grocery.objects.get(name=obj.name)
            grocery.quantity = form.cleaned_data.get("quantity")
            grocery.save()
            form = UpdateForm()
        print("POST")
        return redirect('../')

    queryset = Grocery.objects.all()

    context = {
        "form": form,
        "object": obj,
        "object_list": queryset
    }
    return render(request, "groceries/grocery_update.html", context)


def grocery_delete_overview(request):
    queryset = Grocery.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, 'groceries/grocery_delete_overview.html', context)


def grocery_update_overview(request):
    queryset = Grocery.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, "groceries/grocery_update_overview.html", context)


def grocery_detail_view(request, id):
    obj = get_object_or_404(Grocery, id=id)
    context = {
        "object": obj
    }
    return render(request, "groceries/grocery_detail.html", context)


# LIST OF GROCERY LIST VIEWS --------------------------------------------------------------------------------------------

def grocery_list_overview(request):
    form = GroceryListItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = GroceryListItemForm()

    queryset = Grocery.objects.all()
    groceryitemset = GroceryListItem.objects.all()
    context = {
        "form": form,
        "object_list": queryset,
        "grocery_item_list": groceryitemset
    }

    return render(request, 'groceries/grocery_list_overview.html', context)


def grocery_list_settings_view(request):
    form = GroceryListItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = GroceryListItemForm()

    queryset = Grocery.objects.all()
    groceryitemset = GroceryListItem.objects.all()
    context = {
        "form": form,
        "object_list": queryset,
        "grocery_item_list": groceryitemset
    }

    return render(request, 'groceries/grocery_list_settings.html', context)

# DELETE AN EVENT


def grocery_list_item_delete_view(request, grocerylist_item_id):
    grocery_list_item = GroceryListItem.objects.get(pk=grocerylist_item_id)
    grocery_list_item.delete()
    return redirect('grocery-list-settings-view')


# For testing and developing inventory view with bootstrap  ----------------------------------------------------------
def grocery_development_view(request):
    queryset = Grocery.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, 'groceries/grocery_development.html', context)

# For testing and developing new concepts with bootstrap


def grocery_development_view0(request):
    queryset = Grocery.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, 'groceries/grocery_development_0.html', context)
