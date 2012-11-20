# coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django.http import HttpRequest
from django.template import RequestContext

# Models:
from main.models import Product, Store, Ingredient, Manufacturer, Brand
from django.forms.models import modelformset_factory

newest_vegan = Product.objects.filter(vegan='V').order_by('-created')[:10]

def index(request):

    return render_to_response('index.html',{ 'products_vegan': newest_vegan },
    context_instance=RequestContext(request))

def links(request):

    return render_to_response('links.html',{ 'products_vegan': newest_vegan },
    context_instance=RequestContext(request))

def product_page_by_id(request, product_id):

    pro = Product.objects.get(id=product_id)
    return render_to_response('products.html', 
    {'product': pro, 'products_vegan': newest_vegan},
    context_instance=RequestContext(request))

def ingredient_page_by_id(request, ingredient_id):

    ing = Ingredient.objects.get(id=ingredient_id)
    return render_to_response('ingredients.html', 
    {'ingredient': ing,},
    context_instance=RequestContext(request))

def list_all_products(request):

    products = Product.objects.all()
    return render_to_response('list_results.html', { 'products': products, 'products_vegan': newest_vegan }, 
    context_instance=RequestContext(request))


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
    productForm = modelformset_factory(category, exclude=('verified',))
    if request.method == 'POST':
        formset = productForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("form_received.html", context_instance=RequestContext(request))
            # do something.
    else:
        formset = productForm(queryset=category.objects.none())
    return render_to_response("form_item_add.html", {
        "formset": formset, "category": category, }, context_instance=RequestContext(request))     


def edit_form(request, product_id):
    productForm = modelformset_factory(Product, extra=0, exclude=('verified', 'name'))
    product_info = Product.objects.get(id=product_id)
    if request.method == 'POST':
        formset = productForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("form_received.html", context_instance=RequestContext(request))
            # do something.
    else:
        formset = productForm(queryset=Product.objects.filter(id=product_id))
    return render_to_response("form_item_edit.html", {
        "formset": formset, "product_info": product_info,
    }, context_instance=RequestContext(request))     



# SEARCH:

def search_form(request):
    return render_to_response('search_form.html', context_instance=RequestContext(request))


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        products = Product.objects.filter(name__icontains=q)
        return render_to_response('search_results.html',  {'products': products, 'query': q}, context_instance=RequestContext(request))
    else:
        return HttpResponse('Skriv venligst et søge-term.')

