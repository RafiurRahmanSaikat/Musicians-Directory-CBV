from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("add/", views.add_album.as_view(), name="add_album"),
    path("edit/<int:id>/", views.edit_album.as_view(), name="edit_album"),
]
