# Generated by Django 4.0.6 on 2022-09-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0002_grocerylistitem'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='grocerylistitem',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_item'),
        ),
    ]
