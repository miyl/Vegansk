# coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django.http import HttpRequest
from django.template import RequestContext

# Models:
from main.models import product, store, ingredient, manufacturer, brand
from django.forms.models import modelformset_factory

def index(request):
    return render_to_response('index.html',
    context_instance=RequestContext(request))


def product_page_by_id(request, product_id):
    pro = product.objects.get(id=product_id)
    return render_to_response('products.html', 
    {'product': pro,},
    context_instance=RequestContext(request))


def list_all_products(request):
    products = product.objects.all()
    return render_to_response('list_results.html', { 'products': products }, 
    context_instance=RequestContext(request))


def add_form(request, add_category):
    print("add_category")
    productForm = modelformset_factory(add_category, exclude=('verified',))
    if request.method == 'POST':
        formset = productForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("form_received.html", context_instance=RequestContext(request))
            # do something.
    else:
        formset = productForm(queryset=add_category.objects.none())
    return render_to_response("form_item_add.html", {
        "formset": formset,
    }, context_instance=RequestContext(request))     

def edit_form(request, product_id):
    productForm = modelformset_factory(product, extra=0, exclude=('verified', 'name'))
    product_info = product.objects.get(id=product_id)
    if request.method == 'POST':
        formset = productForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render_to_response("form_received.html", context_instance=RequestContext(request))
            # do something.
    else:
        formset = productForm(queryset=product.objects.filter(id=product_id))
    return render_to_response("form_item_edit.html", {
        "formset": formset, "product_info": product_info,
    }, context_instance=RequestContext(request))     



# SEARCH:

def search_form(request):
    return render_to_response('search_form.html', context_instance=RequestContext(request))


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        products = product.objects.filter(name__icontains=q)
        return render_to_response('search_results.html',  {'products': products, 'query': q}, context_instance=RequestContext(request))
    else:
        return HttpResponse('Skriv venligst et søge-term.')


#def new_search(request):
#    if 'q' in request.GET and request.GET['q']:
#        q = request.GET['q']
#        
#        return render_to_response('search_results.html',  {'products': products, 'query': q}, context_instance=RequestContext(request))
#    else:
#        return HttpResponse('Skriv venligst et søge term.')

#def search_test(request,q=None):
#    if 'q' in request.GET and request.GET['q']:
#        q = request.GET['q']
#	if q is None:
#		return HttpResponse('Please submit a search term.')
#    products = product.objects.filter(name__icontains=q)
#    return render_to_response('search_results.html',  {'products': products, 'query': q}, context_instance=RequestContext(request))
