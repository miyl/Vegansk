#! /usr/bin/env python3

# Copied from manage.py to simulate the same environment:
import os, sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vegansk.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

# The script itself:

from products.models import Brand, Manufacturer, Store, Ingredient, Product
from django.contrib.auth import get_user_model
#from datetime import datetime

# Cleanup
Brand.objects.all().delete()
Manufacturer.objects.all().delete()
Store.objects.all().delete()
Ingredient.objects.all().delete()
Product.objects.all().delete()
get_user_model().objects.filter(username="woop").delete()

u = get_user_model().objects.create_user(username='woop', email='woo@woo.com', password='woop', is_staff=True, is_superuser=True)
u.save()

# Add new data
i=1
while i < 10:
    a = Brand(name="Urtekram" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Brand(name="Rittersport" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Brand(name="Storck" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Manufacturer(name="Urtekram" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Manufacturer(name="Rittersport" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Manufacturer(name="Storck" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Store(name="Kvickly" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Store(name="Fakta" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Store(name="Foetex" + str(i), only_vegan_products=False, verified=True, added_by=u)
    a.save()
    a = Ingredient(name="Roersukker" + str(i), vegan='P', verified=True)
    a.save()
    a = Ingredient(name="Carminer" + str(i), alias1="e120", vegan='N', verified=True)
    a.save()
    a = Ingredient(name="Vegetabilsk olie" + str(i), vegan="V", verified=True, added_by=u)
    a.save()
    i+=1

"""
# a = Product(name="Mamba", vegan='V', brands="Storck", manufacturers="Urtekram", stores="Kvickly, Fakta", ingredients="Roersukker, Vegetabilsk olie", picture="/media/product_images/hexagon_800.gif" )
    a = Product(name="Mamba", vegan='V', picture="/media/product_images/hexagon_800.gif" )
    a.save()

    a = Product.objects.get(pk=1)
    brand = Brand.objects.get(name="Storck")
    Product.brands = brand
    a.save()

    a = Product.objects.get(pk=1)
    manufacturer = Manufacturer.objects.get(name="Storck")
    Product.manufacturers = manufacturer
    a.save()

    a = Product.objects.get(pk=1)
    store = Store.objects.get(name="Kvickly")
    Product.stores = store
    a.save()

    product = Product.objects.get(pk=1)
    ingredient = Ingredient.objects.get(name="Roersukker")
    Product.ingredients = ingredient
    product.save()
# a = Product(name="Rittersport Marcipan", vegan='V', Brand="Rittersport", Manufacturer="Rittersport", Store="Foetex, Fakta", Ingredient="Roersukker", picture="/media/product_images/hexagon_800.gif" )
# a.save()
# a = Product(name="Lakridspiber", vegan='N', Brand="Urtekram", Manufacturer="Storck", Store="Fakta", Ingredient="Carminer, Vegetabilsk olie", picture="/media/product_images/hexagon_800.gif" )
# a.save()
    i+=1

#    time = datetime.now()
# b = Event(name="Name" + str(i), starts=time, ends=time, description="Description " * 50 + str(i),poster="/media/posters/My-Little-Pony-Friendship-Is-Magic-Season-2-Episode-7-May-the-Best-Pet-Win-.jpg")
"""
