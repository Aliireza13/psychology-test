from django.urls import path

from . import views



app_name = "core"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/user/add/", views.add_user, name="add_user"),
    path("dashboard/user/<int:user_id>/", views.user_detail, name="user_info"),
    path("dashboard/user/<int:user_id>/<int:test_id>/", views.user_answers, name="user_answers"),
]
