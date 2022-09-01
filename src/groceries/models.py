from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Grocery(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.SmallIntegerField()
    store = models.CharField(max_length=30)

    def get_absolute_url(self):
        #print(reverse_lazy("grocery-detail", kwargs={"id": self.id}))
        return reverse_lazy("grocery-detail", kwargs={"id": self.id})

class GroceryListItem(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.SmallIntegerField()

    def get_absolute_url(self):
        #print(reverse_lazy("grocery-detail", kwargs={"id": self.id}))
        return reverse_lazy("grocery-detail", kwargs={"id": self.id})