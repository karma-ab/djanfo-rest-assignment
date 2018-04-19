from __future__ import unicode_literals
from django.db import migrations


def create_initial_products(apps, schema_editor):
    Product = apps.get_model('userActivity', 'Post')

    Product(name='Salame').save()
    Product(name='Olio Balsamico').save()



class Migration(migrations.Migration):

    dependencies = [
        ('userActivity', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_products),
    ]
