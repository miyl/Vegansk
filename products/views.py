# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
#from django.http import HttpRequest

# Models:
from products.models import Product, Store, Ingredient, Manufacturer, Brand
from django.forms.models import modelformset_factory

newest_vegan = Product.objects.filter(vegan='V').order_by('-created')[:10]

def index(request):

    return render(request, 'index.html',{ 'products_vegan': newest_vegan })

def links(request):

    return render(request, 'links.html',{ 'products_vegan': newest_vegan })

def product_page_by_id(request, product_id):

    pro = Product.objects.get(id=product_id)
    return render(request, 'products.html', {'product': pro, 'products_vegan': newest_vegan})

def ingredient_page_by_id(request, ingredient_id):

    ing = Ingredient.objects.get(id=ingredient_id)
    return render(request, 'ingredients.html', {'ingredient': ing,})

def list_all_products(request):

    products = Product.objects.all()
    return render(request, 'list_results.html', { 'products': products, 'products_vegan': newest_vegan })


def add_form(request, category):
    if category == 'product':
        category = Product
    if category == 'ingredient':
        category = Ingredient
    if category == 'manufacturer':
        category = Manufacturer
    if category == 'store':
        category = Store
    if category == 'brand':
        category = Brand
    catName = category._meta.verbose_name
    productForm = modelformset_factory(category, exclude=('verified','featured'))
    if request.method == 'POST':
        formset = productForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render(request, "form_received.html", {})
            # do something.
    else:
        formset = productForm(queryset=category.objects.none())
    return render(request, "form_item_add.html", { "formset": formset, "category": category,"catName": catName })


def edit_form(request, product_id):
    productForm = modelformset_factory(Product, extra=0, exclude=('verified', 'name', 'featured'))
    product_info = Product.objects.get(id=product_id)
    if request.method == 'POST':
        formset = productForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render(request, "form_received.html", {})
            # do something.
    else:
        formset = productForm(queryset=Product.objects.filter(id=product_id))
    return render(request, "form_item_edit.html", { "formset": formset, "product_info": product_info, })



# SEARCH:

def search_form(request):
    return render(request, 'search_form.html', {})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        products = Product.objects.filter(name__icontains=q)
        return render(request, 'search_results.html',  {'products': products, 'query': q})
    else:
        return HttpResponse('Skriv venligst et søge-term.')

