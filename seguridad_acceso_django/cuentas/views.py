from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistroConEmailForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class AdminDataView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'datos_sensibles.html'
    context_object_name = 'usuarios'  
    permission_required = 'auth.view_user' 
    raise_exception = True  


class RegistroUsuarioView(CreateView):
    model = User
    form_class = RegistroConEmailForm 
    template_name = 'registrar/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "¡Registro exitoso! Ya puedes iniciar sesión.")
        return response