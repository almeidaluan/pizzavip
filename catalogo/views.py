from django.shortcuts import render,get_object_or_404

from .models import Product,Category

from django.views import generic

#Lista todos os produto
class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalogo/product_list'
    context_object_name = 'products'
    paginate_by = 2

product_list = ProductListView.as_view()

#Mostra os Detalhes do produt
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalogo/product.html'


product = ProductDetailView.as_view()


#Lista todos os produtos do tamanho P de acordo com a categori
class CategoryListView(generic.ListView):
    template_name = 'catalogo/category.html'
    context_object_name = 'product_list'
    paginate_by = 5

    def get_queryset(self):
        size = self.request.GET.get('size','P')
        return Product.objects.filter(category__slug=self.kwargs['slug'],

                                        size=size)

    def get_context_data(self,**kwargs):
        context = super(CategoryListView,self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category,slug=self.kwargs['slug'])
        #context['teste'] = Product.objects.filter(category__slug=self.kwargs['slug'],size='M')
        return context

category = CategoryListView.as_view()



#Lista os Produtos com base em sua categoria - Forma Normal
#def category(request,slug):
#    category=Category.objects.get(slug=slug)
#    context = {
#        'current_category':category,
#        'product_list':Product.objects.filter(category=category),
#    }
#    return render(request,'catalogo/category.html',context)


#Pega o produto especifico - Forma Normal
#def product(request,slug):
#    product = Product.objects.get(slug=slug)
#    context = {
#        'product':product
#    }

#    return render(request,'catalogo/product.html',context)
