
from django.conf.urls import url
from django.contrib import admin

from .views import (
    contact,
    index,


)

urlpatterns = [
    url(r'^$',index,name="index"),
    url(r'^contato/$',contact,name="contact"),

    #url(r'^inicio/$',inicio,name="inicio"),


]
