from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#For development, media_root:
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from products import views

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'id/<int:product_id>/', views.product_page_by_id, name="product_page_by_id"),
    path(r'ingredient/id/<int:ingredient>/', views.ingredient_page_by_id, name="ingredient_page_by_id"),
    path(r'produktliste/', views.list_all_products, name="list_all"),
    path(r'soege-formular/', views.search_form, name="search_form"),
    path(r'soeg/', views.search, name="search"),
    path(r'tilfoej/(<str:category>/', views.add_form, name="add_form"),
    path(r'id/<int:product_id>/rediger/', views.edit_form, name="edit_form"),
    path(r'links/', views.links, name="links"),
    #url(r'comments/', include('django.contrib.comments.urls')),


#   url(r'tilfoej-produkt/$', 'add_form', name="add_form"),
#   url(r'tilfoej-(?P<add_category>\[a-z]*)/$', 'add_form', name="add_form"),
#   url(r'produkt/(?P<q>[0-9a-zA-Z-]+)?/$', 'search_test', name="search_test"),
#   url(r'search-results/$', views.search),


    # Examples:
    # url(r'', 'vegansk.views.home', name='home'),
    # url(r'vegansk/', include('vegansk.foo.urls')),

    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),

    #path(r'login/', 'django.contrib.auth.views.login', name="login"),
    #path(r'logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # url(r'create/', 'django.views.generic.create_update.create_object', {'model': 'products.product'}),
]

#For development, media_root:
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    #urlpatterns += [
    #    (r'media/(?P<path>.*)', 'django.views.static.serve', {
    #    'document_root': settings.MEDIA_ROOT})
    #]
