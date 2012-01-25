from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from vegansk.main.models import product, store, ingredient

def index(request):
    return render_to_response('index.html',
    context_instance=RequestContext(request))


def product_id(request, product_id):
    pro = product.objects.get(id=product_id)

    return render_to_response('products.html', 
    						  {'product': pro,},
							  context_instance=RequestContext(request))
    #return HttpResponse("You're looking at the results of poll %s." % product_id)


def search_form(request):
    return render_to_response('search_form.html', context_instance=RequestContext(request))


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        products = product.objects.filter(name__icontains=q)
        return render_to_response('search_results.html',  {'products': products, 'query': q}, context_instance=RequestContext(request))
    else:
        return HttpResponse('Please submit a search term.')


def search_test(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        products = product.objects.filter(name__icontains=q)
        return render_to_response('search_results.html',  {'products': products, 'query': q}, context_instance=RequestContext(request))
    else:
        return HttpResponse('Please submit a search term.')


def list_all(request):
    products = product.objects.all()
    return render_to_response('list_results.html', { 'products': products }, 
            context_instance=RequestContext(request))
