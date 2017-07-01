from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import CartItem
from django.views.generic import RedirectView,TemplateView,ListView,DetailView
from catalogo.models import Product
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CartItem, Order
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from pagseguro import PagSeguro
# Responsavel por adicionar o Produto no carrinho | primeira parte no models.py
class CreateCartItemView(RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request,'Produto Adicionado com Sucesso')
        else:
            messages.success(self.request,'Produto Atualizado com Sucesso')
        return  reverse('checkout:cart_item')            #product.get_absolute_url()

create_cartitem = CreateCartItemView.as_view()

# Responsavel por renderizar os itens na pagina de carrinho utilizando model form set
class CartItemView(TemplateView):

    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(CartItem,fields=('quantity',),can_delete=True,extra=0)
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(queryset=CartItem.objects.filter(cart_key=session_key))
            else:
                formset = CartItemFormSet(queryset=CartItem.objects.filter(cart_key=session_key),data=self.request.POST or None)
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self,**kwargs):
        context =super(CartItemView,self).get_context_data(**kwargs)
        context['formset']  = self.get_formset()
        return context

    def post(self,request,*args,**kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request,"Carrinho Atualizado com sucesso")
        context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)


cart_item = CartItemView.as_view()


class CheckoutView(LoginRequiredMixin,TemplateView):
    template_name = 'checkout/checkout.html'

    def get(self,request,*args,**kwargs):
        session_key = request.session.session_key
        
        if session_key and CartItem.objects.filter(cart_key=session_key).exists():
            cart_itens = CartItem.objects.filter(cart_key=session_key)
            order = Order.objects.create_order(
                user=request.user,cart_itens=cart_itens
            )
        else:
            messages.info(request,'Não há itens no carrinho de compras')
            return redirect('checkout:cart_item')
        response = super(CheckoutView,self).get(request,*args,**kwargs)
        response.context_data['order'] = order
        
        return response

checkout = CheckoutView.as_view()


class OrderListView(LoginRequiredMixin, ListView):

    template_name = 'checkout/order_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('pk')

orderlist = OrderListView.as_view()


class OrderDetailView(LoginRequiredMixin,DetailView):

    template_name = 'checkout/order_detail.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


orderdetail = OrderDetailView.as_view()



#PARTE DO PAGSEGURO PARA EXPLICAR


class PagSeguroView(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        order_pk = self.kwargs.get('pk')
        order = get_object_or_404(
            Order.objects.filter(user=self.request.user), pk=order_pk
        )
        pg = order.pagseguro()
        pg.redirect_url = self.request.build_absolute_uri(
            reverse('checkout:order_detail', args=[order.pk])
        )
        pg.notification_url = self.request.build_absolute_uri(
            reverse('checkout:pagseguro_notification')
        )
        response = pg.checkout()
        return response.payment_url



pagseguro_view = PagSeguroView.as_view()

@csrf_exempt
def pagseguro_notification(request):
    notification_code = request.POST.get('notificationCode',None)
    if notification_code:
        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL,token=settings.PAGSEGURO_TOKEN,
            config={'sandbox':settings.PAGSEGURO_SANDBOX}
    
        )
        notification_data = pg.check_notification(notification_code) #envia um codigo de notificação e com base na requisição voce sabe as informações
        status = notification_data.status #status pagseguro
        reference = notification_data.reference #nosso id de pedido
        try:
            order = Order.objects.get(pk=reference)
        except Order.DoesNotExist:
            pass
        else:
            order.pagseguro_update_status(status)
        return HttpResponse('OK')
    

