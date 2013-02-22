from django import template
from products.models import Product, Store, Ingredient, Manufacturer, Brand

register = template.Library()

@register.simple_tag 
def get_verbose_name(object): 
    return Product._meta.verbose_name
    #return queryset.model._meta.verbose_name
