from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import LinkCutterForm
from .models import Url


# ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ РЕГИСТРАЦИИ
class RegisterUserView(FormView):
    form_class = UserCreationForm
    template_name = 'main/registration.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super(RegisterUserView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterUserView, self).form_invalid(form)


# ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ АВТОРИЗАЦИИ
class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    success_url = '/'

    def get_success_url(self):
        return self.success_url


# ПРАДСТАВЛЕНИЕ ЛОГАУТА
class Logout(LogoutView):
    next_page = '/login'


# ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ СОКРАЩЕНИЯ ССЫЛКИ
def cutview(request):
    if request.user.is_authenticated == True:
        form = LinkCutterForm
        return render(request, 'main/cut.html', {'form': form})
    else:
        return redirect("login")



# СОЗДАНИЕ ОБЪЕКТА ССЫЛКИ В БАЗУ ДАННЫХ И ВЫВОД В HTML С ПОМОЩЬЮ AJAX
def ajax_posting(request):
    if request.is_ajax():
        user = request.user
        full_url = request.POST.get('full_url', None)
        if full_url:
            try:
                Url.objects.create(
                    full_url=full_url,
                    user=user,
                )
            except IntegrityError:
                print('такая ссылка уже существует')

            url_hash = Url.objects.filter(full_url=full_url).first().url_hash


            response = {
                         'msg':'Your form has been submitted successfully',
                         'full_url': full_url,
                         'url_hash': url_hash
            }
            return JsonResponse(response)


# ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ ПРОСМОТРА СВОИХ ССЫЛОК
def users_urls(request):
    if request.user.is_authenticated == True:
        user = request.user
        urls = Url.objects.filter(user=user)
        return render(request, 'main/my_urls.html', {'urls': urls})
    else:
        return redirect("login")


# ПРЕДСТАВЛЕНИЕ РЕДИРЕКТА НА ОРИГИНАЛЬНУЮ ССЫЛКУ
def get_existing_short_url(request, str):
    url = Url.objects.filter(url_hash=str).first()
    print(url)
    return redirect(url.full_url)



