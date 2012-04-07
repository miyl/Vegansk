from django.contrib import admin
from models import Brand, Manufacturer, Store, Ingredient, Product

class GeneralAdmin(admin.ModelAdmin):
    search_fields = ('name',)

# For some reason it doesn't sort by brands and manufacturers [foreign key fields], and store does not have its verbose name.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'brands', 'last_updated','id')
    list_filter = ('vegan', 'brands', 'manufacturers', 'stores', 'ingredients', 'bio', 'fair_trade', 'gluten', 'soy', 'nuts')
    date_hierarchy = 'last_updated'
    ordering = ('-last_updated',)
#    filter_horizontal = ('store',)
#    raw_id_fields = ('brand','manufactured_by')

admin.site.register(Brand, GeneralAdmin)
admin.site.register(Manufacturer, GeneralAdmin)
admin.site.register(Store, GeneralAdmin)
admin.site.register(Ingredient, GeneralAdmin)
admin.site.register(Product, ProductAdmin)
