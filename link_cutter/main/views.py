from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import LinkCutterForm
from .models import Url, domain


class RegisterUserView(FormView):
    """Представление страницы регистрации"""
    form_class = UserCreationForm
    template_name = 'main/registration.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        print(form.instance)
        return super(RegisterUserView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterUserView, self).form_invalid(form)


class LoginUserView(LoginView):
    """Представление страницы аутентификации"""
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    success_url = '/'

    def get_success_url(self):
        return self.success_url


class Logout(LogoutView):
    """Представление логаута"""
    next_page = '/login'


class CutView(LoginRequiredMixin, FormView):
    """Представление страницы сокращения ссылки"""
    form_class = LinkCutterForm
    template_name = 'main/cut.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        form = LinkCutterForm(request.POST)
        if form.is_valid():
            full_url = form.cleaned_data['full_url']
            if full_url:
                try:
                    Url.objects.create(
                        full_url=full_url,
                        user=user,
                    )
                except IntegrityError:
                    print('такая ссылка уже существует')
                url_hash = Url.objects.filter(full_url=full_url).first().url_hash

        return render(request, 'main/cut.html', {
            'form': form,
            'full_url': full_url,
            'url_hash': url_hash,
        })


def users_urls(request):
    """Представление страницы просмотра своих ссылок"""
    if request.user.is_authenticated is True:
        user = request.user
        urls = Url.objects.filter(user=user)
        return render(request, 'main/my_urls.html', {'urls': urls, 'domain': domain})
    else:
        return redirect("login")


def get_existing_short_url(request, str):
    """Представление редиректа на оригинальную ссылку"""
    url_hash = domain + str
    url = Url.objects.filter(url_hash=url_hash).first()
    return redirect(url.full_url)
