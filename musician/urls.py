from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.add_musician.as_view(), name="add_musician"),
    path("edit/<int:id>", views.edit_musician.as_view(), name="edit_musician"),
    path("delete/<int:id>", views.delete_musician.as_view(), name="delete_musician"),
]
