from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import MusicForm
from .models import MusicianModel


@method_decorator(login_required, name="dispatch")
class add_musician(CreateView):
    model = MusicianModel
    form_class = MusicForm
    template_name = "add_musician.html"
    success_url = reverse_lazy("home")


@method_decorator(login_required, name="dispatch")
class edit_musician(UpdateView):
    model = MusicianModel
    form_class = MusicForm
    template_name = "add_musician.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


@method_decorator(login_required, name="dispatch")
class delete_musician(DeleteView):
    model = MusicianModel
    template_name = "delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")
