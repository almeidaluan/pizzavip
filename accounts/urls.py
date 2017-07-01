
from django.conf.urls import url

from .views import(
    register,
    index,
    UpdateUser,
    UpdatePassword,
    AlterarDados,
    register2
    )

urlpatterns = [
    url('registro/',register,name="registro"),
    url('^$',index,name="index"),
    url('alterar-senha/$',UpdatePassword,name="UpdatePassword"),
    url('alterar-dados/$',UpdateUser,name="UpdateUser"),
    url('alterar-dados2/',AlterarDados,name="alterardados"),
    url('registro2/',register2,name="registro2"),

]
