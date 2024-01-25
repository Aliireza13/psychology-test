from django.urls import path

from . import views



app_name = "core"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/user/<pk>", views.user_detail, name="user_info"),
]
