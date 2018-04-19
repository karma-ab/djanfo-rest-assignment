from __future__ import unicode_literals
from django.db import migrations


def create_initial_products(apps, schema_editor):
    Product = apps.get_model('userActivity', 'Post')

    Product(name='Salame', login='SalameToscano', logout='Asalame').save()
    Product(name='Olio Balsamico', login='Olio balsamico di Modena', logout='Alioa').save()



class Migration(migrations.Migration):

    dependencies = [
        ('userActivity', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_products),
    ]
