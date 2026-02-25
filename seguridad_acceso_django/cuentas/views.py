from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class AdminDataView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'datos_sensibles.html'
    permission_required = 'auth.view_user' 
    raise_exception = True