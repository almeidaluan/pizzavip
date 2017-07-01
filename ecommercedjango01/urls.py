"""ecommercedjango01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, inclu
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^', include('util.urls',namespace='util')),
    url(r'^login/$',auth_views.login,{'template_name':'login.html'},name="login"),
    url(r'^sair/$',auth_views.logout,{'next_page':'util:index'},name="logout"),
    url(r'^catalogo/',include('catalogo.urls',namespace='catalogo')),
    url(r'^admin/',admin.site.urls),
    url('conta/',include('accounts.urls',namespace='accounts')),
    url('compras/',include('checkout.urls',namespace='checkout')),
]
