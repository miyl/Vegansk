from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name="index"),
	url(r'^id/(?P<product_id>\d+)/$', 'main.views.product_id'),
	url(r'^product/(?P<q>\d+)/$', 'main.views.search_test'),
    url(r'^produkter/$', 'main.views.list_all'),
    url(r'^search/$', 'main.views.search', name="search"),
    url(r'^search-form/$', 'main.views.search_form', name="search_form"),
#    (r'^search-results/$', views.search),
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

