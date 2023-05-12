from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Vehicle
from .forms import VehicleForm
from django.views.generic.base import TemplateView


# SuperAdmin View

class VehicleHomeView(ListView):
    model = Vehicle
    context_object_name = 'home'
    template_name = 'home.html'


class SuperAdminVehicleListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class SuperAdminVehicleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    context_object_name = 'vehicle'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class SuperAdminVehicleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle_management:superadmin_vehicle_list')
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class SuperAdminVehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle_management:superadmin_vehicle_list')
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


class SuperAdminVehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_management:superadmin_vehicle_list')
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser


# Admin View
class AdminVehicleListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff


class AdminVehicleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    context_object_name = 'vehicle'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff


class AdminVehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_management/vehicle_form.html'
    success_url = reverse_lazy('vehicle_management:admin_vehicle_list')
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff


# User View
class UserVehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_management/vehicle_list.html'
    context_object_name = 'vehicles'
    login_url = 'login'

    def get_queryset(self):
        return Vehicle.objects.all().order_by('vehicle_number')


class ProfileView(TemplateView):
    template_name = 'profile.html'