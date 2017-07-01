from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView,FormView,DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from .forms import UserAdminCreationForm,UserCreationForm
from ecommercedjango01.settings import LOGIN_REDIRECT_URL,LOGIN_REDIRECT_URL_REGISTER,UPDATE_REDIRECT_URL
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

#View Cadastro de usuari
class RegisterView(CreateView):
    model = User
    template_name = 'accounts/cadastro.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy(LOGIN_REDIRECT_URL_REGISTER)

register = RegisterView.as_view()


class RegisterView2(CreateView):
    model = User
    template_name = 'accounts/cadastro2.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy(LOGIN_REDIRECT_URL_REGISTER)

register2 =RegisterView2.as_view()


#View Minha Conta
class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "accounts/index.html"

index = IndexView.as_view()


#Responsavel pela alteração do usuario
class UpdateUser(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = User
    template_name = 'accounts/update-user.html'
    fields = ['name','email','complemento','numero','logradouro','cidade','telefone']
    success_url = reverse_lazy(UPDATE_REDIRECT_URL)
    success_message = "Alterado com sucesso"

    def get_object(self):
        return self.request.user

UpdateUser = UpdateUser.as_view()



class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm
    success_message = "Alterado com sucesso"

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self,form):
        form.save()
        return super(UpdatePasswordView,self).form_valid(form)

UpdatePassword = UpdatePasswordView.as_view()



class AlterarDados(LoginRequiredMixin,TemplateView):
    model = User
    template_name = 'accounts/alterar-dados.html'


AlterarDados = AlterarDados.as_view()
