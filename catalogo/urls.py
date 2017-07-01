
from django.conf.urls import url
from django.contrib import admin

from .views import (
    category,
    product,
    product_list,
)

urlpatterns = [

    #url(r'^produto/$',product,name="product"),
    url(r'^$',product_list,name="product_list"),
    url(r'^(?P<slug>[\w_-]+)/$',category,name="category"),

    url(r'^produto/(?P<slug>[\w_-]+)/$',product,name="product"),

]
