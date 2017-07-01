
from django.conf.urls import url
from django.contrib import admin

from . views import(
create_cartitem,
cart_item,
checkout,
orderlist,
orderdetail,
pagseguro_view,

)
from . import views

urlpatterns = [

    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$',create_cartitem,name='create_cartitem'),
    url(r'^carrinho/$',cart_item,name='cart_item'),
    url(r'^finalizando/$',checkout, name='checkout'),
    url(r'^meus-pedidos/$',orderlist, name='order_list'),
    url(r'^meus-pedidos/(?P<pk>\d+)/$',orderdetail, name='order_detail'),
    
    url(r'^finalizando/(?P<pk>\d+)/pagseguro/$',pagseguro_view, name='pagseguro_view'),
    url(r'^notificacoes/pagseguro/$',views.pagseguro_notification,name='pagseguro_notification'),



]
