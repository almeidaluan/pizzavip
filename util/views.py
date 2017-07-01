# coding=utf-8

from django.shortcuts import render

from django.http import HttpResponse

from catalogo.models import Category
from django.shortcuts import get_object_or_404
from catalogo.models import Product,Category

from .forms import ContatoForm

from django.core.mail import send_mail

from django.conf import settings

from django.views.generic import TemplateView,ListView,CreateView
from django.core.urlresolvers import reverse



#Responsavel pela lista de refrigerantes e pizzas da pagina inicial
def index(request):

    size = request.GET.get('size','P')
    pizzas = Product.objects.filter(category__slug='pizzas',size=size)
    refrigerantes = Product.objects.filter(category__slug='bebidas',size=size)
    #caso queira a forma antiga descomentar as 2 linhas de baixo
    #pizzas = Product.objects.filter(category__id=5)[:4]
    #refrigerantes = Product.objects.filter(category__id=6)[:4]

    #pega=Category.objects.get(slug='pizza') esta aki inutilmente
    get_absolute = reverse('catalogo:category',kwargs={'slug':'pizzas'})

    context={
        'pizzas':pizzas,
        'refrigerantes':refrigerantes,
        'get_absolute':get_absolute,

    }

    return render(request,'inicio.html',context)

#Responsavel pelo form e envio de email para contato
def contact(request):
    success = False
    if request.method =='POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email =form.cleaned_data['email']
            message =form.cleaned_data['message']
            message = 'Nome:{0}\nEmail:{1}\n{2}'.format(name,email,message)
            send_mail('Contato do Django Ecommerce',message,settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])
            success = True
            form = ContatoForm()
    else:
        form = ContatoForm()
    context = {
        'form':form,
        'success':success
    }
    return render(request, 'contact.html',context)



    #class IndexView(ListView):

     #    model = Product
      #   template_name = 'catalogo/product_list'
      #   context_object_name = 'products'
       #  paginate_by = 5


    #index = IndexView.as_view()
