from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','name','email','telefone','logradouro','numero','complemento','cpf','cidade']

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','name','telefone','logradouro','numero','complemento','cpf','cidade','is_active','is_staff']
