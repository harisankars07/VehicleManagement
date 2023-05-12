from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    SuperAdminVehicleListView,
    SuperAdminVehicleDetailView,
    SuperAdminVehicleCreateView,
    SuperAdminVehicleUpdateView,
    SuperAdminVehicleDeleteView,
    AdminVehicleListView,
    AdminVehicleDetailView,
    AdminVehicleUpdateView,
    UserVehicleListView, VehicleHomeView,
)
from django.contrib.auth.decorators import login_required
from vehicle_management.views import ProfileView

app_name = 'vehicle_management'

urlpatterns = [
    path('', VehicleHomeView.as_view(), name='home'),
    path('superadmin/vehicle/list/', SuperAdminVehicleListView.as_view(), name='superadmin_vehicle_list'),
    path('superadmin/vehicle/<int:pk>/', SuperAdminVehicleDetailView.as_view(), name='superadmin_vehicle_detail'),
    path('superadmin/vehicle/create/', SuperAdminVehicleCreateView.as_view(), name='superadmin_vehicle_create'),
    path('superadmin/vehicle/<int:pk>/update/', SuperAdminVehicleUpdateView.as_view(), name='superadmin_vehicle_update'),
    path('superadmin/vehicle/<int:pk>/delete/', SuperAdminVehicleDeleteView.as_view(), name='superadmin_vehicle_delete'),
    path('admin/vehicle/list/', AdminVehicleListView.as_view(), name='admin_vehicle_list'),
    path('admin/vehicle/<int:pk>/', AdminVehicleDetailView.as_view(), name='admin_vehicle_detail'),
    path('admin/vehicle/<int:pk>/update/', AdminVehicleUpdateView.as_view(), name='admin_vehicle_update'),
    path('user/vehicle/list/', UserVehicleListView.as_view(), name='user_vehicle_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/profile/', login_required(ProfileView.as_view()), name='profile'),
]
