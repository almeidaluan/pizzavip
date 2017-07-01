from django.contrib import admin

# Register your models here.

from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name','slug','created']
    search_fields = ['name','slug']
    list_filter = ['created','modified']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','description','price','size','created','modified']
    search_fields = ['name','slug','category__name','description','price','size','created','modified']
    list_filter= ['created','modified']
    #lookup para buscar produto pela category



admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
