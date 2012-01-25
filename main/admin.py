from django.contrib import admin
from vegansk.main.models import brand, manufacturer, store, ingredient, product

class generalAdmin(admin.ModelAdmin):
    search_fields = ('name',)


# For some reason it doesn't sort by brands and manufacturers [foreign key fields], and store does not have its verbose name.
class productAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'brands', 'last_updated','id')
    list_filter = ('vegan', 'brands', 'manufacturers', 'stores', 'ingredients', 'bio', 'fair_trade', 'gluten', 'soy', 'nuts')
    date_hierarchy = 'last_updated'
    ordering = ('-last_updated',)
#    filter_horizontal = ('store',)
#    raw_id_fields = ('brand','manufactured_by')

admin.site.register(brand, generalAdmin)
admin.site.register(manufacturer, generalAdmin)
admin.site.register(store, generalAdmin)
admin.site.register(ingredient, generalAdmin)
admin.site.register(product, productAdmin)
