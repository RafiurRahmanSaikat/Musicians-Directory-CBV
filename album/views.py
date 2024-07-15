from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, RedirectView, UpdateView

from .forms import AlbumForm
from .models import AlbumModel

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "SignUp"
        return context


class UserLoginView(LoginView):
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Login successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid credentials")
        return super().form_invalid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("home")


class LogoutView(RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


@method_decorator(login_required, name="dispatch")
class add_album(CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = "add_album.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class edit_album(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = "add_album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")
