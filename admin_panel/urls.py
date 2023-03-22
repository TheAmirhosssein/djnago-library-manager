from django.urls import path

from admin_panel import views

urlpatterns = [path("", views.DashboardView.as_view(), name="admin")]
