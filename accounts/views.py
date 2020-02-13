from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .form import LoginForm, RegisterForm


class Login(LoginView):
    """
    LoginView:
    """
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        # すでにログインしている場合はToDoへリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('todo:index'))

        context = {
            'form': LoginForm(),
        }

        return render(request, 'accounts/login.html', context)


class Logout(LogoutView):
    """
    LogoutView:
    """
    template_name = 'accounts/logout.html'


class Register(CreateView):
    """
    user新規作成View
    """
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('todo:index')

    def get(self, request, *args, **kwargs):
        # すでにログインしている場合はToDoへリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('todo:index'))

        context = {
            'form': RegisterForm(),
        }
        return render(request, 'accounts/register.html', context)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        auth_login(self.request, user)

        return super().form_valid(form)
