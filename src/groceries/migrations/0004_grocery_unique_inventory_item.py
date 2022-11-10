# Generated by Django 4.0.6 on 2022-09-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0003_grocerylistitem_unique_item'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='grocery',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_inventory_item'),
        ),
    ]
