from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .forms import GroceryForm, GroceryListItemForm, UpdateForm
from .models import Grocery, GroceryListItem
from django.contrib.auth.models import User

# reportlab imports
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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
        form.save(request.user.get_username())
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
            grocery = Grocery.objects.get(
                name=obj.name, username=request.user.get_username())
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
        form.save(request.user.get_username())
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
        form.save(request.user.get_username())
        form = GroceryListItemForm()

    queryset = Grocery.objects.all()
    groceryitemset = GroceryListItem.objects.all()
    context = {
        "form": form,
        "object_list": queryset,
        "grocery_item_list": groceryitemset
    }

    return render(request, 'groceries/grocery_list_settings.html', context)

# Generated view of grocery list, subtracts the quantity of an item with the quantity the client wants to keep up with their inventory


def grocery_list_generated_view(request):
    groceryitemset = GroceryListItem.objects.filter(
        username=request.user.get_username())

    finalgrocerylistset = []
    for listitem in groceryitemset:
        itemininventory = Grocery.objects.filter(
            name=listitem.name, username=request.user.get_username())
        if (len(itemininventory) == 0):
            finalgrocerylistset.append(listitem)
        else:
            ininventory = Grocery.objects.get(
                name=listitem.name, username=request.user.get_username())
            missingquantity = listitem.quantity - ininventory.quantity
            # If missing quantity is greater than 0 that means there are not enough items in the inventory to satisfy the requirements on the list. In that case, add the difference between them as a new grocerylist item and put it on the list.
            if (missingquantity > 0):
                itemtobeadded = listitem
                itemtobeadded.quantity = missingquantity
                finalgrocerylistset.append(itemtobeadded)

    context = {
        "grocery_item_list": finalgrocerylistset
    }

    return render(request, 'groceries/grocery_list_generated.html', context)

# DELETE AN EVENT


def grocery_list_item_delete_view(request, grocerylist_item_id):
    grocery_list_item = GroceryListItem.objects.get(pk=grocerylist_item_id)
    grocery_list_item.delete()
    return redirect('grocery-list-settings-view')


# Generate a grocery list in the form of a pdf file
def generated_pdf_view(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    groceryitemset = GroceryListItem.objects.filter(
        username=request.user.get_username())

    finalgrocerylistset = []
    for listitem in groceryitemset:
        itemininventory = Grocery.objects.filter(
            name=listitem.name, username=request.user.get_username())
        if (len(itemininventory) == 0):
            finalgrocerylistset.append(listitem)
        else:
            ininventory = Grocery.objects.get(
                name=listitem.name, username=request.user.get_username())
            missingquantity = listitem.quantity - ininventory.quantity
            # If missing quantity is greater than 0 that means there are not enough items in the inventory to satisfy the requirements on the list. In that case, add the difference between them as a new grocerylist item and put it on the list.
            if (missingquantity > 0):
                itemtobeadded = listitem
                itemtobeadded.quantity = missingquantity
                finalgrocerylistset.append(itemtobeadded)

    for line in finalgrocerylistset:
        textob.textLine(line.name + ' (' + str(line.quantity) + ')')

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='grocerylist.pdf')


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
