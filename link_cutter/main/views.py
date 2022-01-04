from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import LinkCutterForm
from .models import Url
from django.contrib.auth.mixins import LoginRequiredMixin
from time import sleep
import json


def home(request):
    return render(request, 'main/index.html')


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
    success_url = '/cut'

    def get_success_url(self):
        return self.success_url


# ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ СОКРАЩЕНИЯ ССЫЛКИ
class CutView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Url
    template_name = 'main/cut.html'
    form_class = LinkCutterForm
    success_url = '/cut'
    login_url = '/login'
    # success_message = 'win'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        print(self.object.full_url)

        self.object.save()
        print(self.object.url_hash)
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = LinkCutterForm()
        if self.request.method == 'POST':
            context['nick'] = self.request.POST.get('url_hash')
            print(self.request.method)

        else:
            context['nick'] = 'suka'
            return context




def cutviewajax(request):
    urls = Url.objects.all()
    response_data = {}
    if request.POST.get('action') == 'post':
        full_url = request.POST.get('full_url')
        response_data['full_url'] = full_url
        user = request.user
        url_hash = request.POST.get('url_hash')
        response_data['url_hash'] = url_hash
        Url.objects.create(
            full_url = full_url,
            user = user,
            url_hash = url_hash
            )
        return JsonResponse(response_data)


    return render(request, 'main/cut.html', {'urls':urls})


def cutview(request):
    if request.method == 'post':
        form = LinkCutterForm(request.POST)
        print('koko')
    else:
        form = LinkCutterForm()
        print('ooo')

    return render(request, 'main/cut.html', {'form':form})





# ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ ПРОСМОТРА СВОИХ ССЫЛОК
def users_urls(request):
    user = request.user
    urls = Url.objects.filter(user=user)
    return render(request, 'main/my_urls.html', {'urls': urls})



# ПРЕДСТАВЛЕНИЕ РЕДИРЕКТА НА ОРИГИНАЛЬНУЮ ССЫЛКУ
def get_existing_short_url(request, str):
    url = get_object_or_404(Url, url_hash=str)
    return redirect(url.full_url)




class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        print(self.object.full_url)

        self.object.save()
        print(self.object.url_hash)
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)
        else:
            return response

class AuthorCreate(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Url
    template_name = 'main/cut.html'
    form_class = LinkCutterForm
    success_url = '/cut'
    login_url = '/login'


def test(request):
    return render(request, 'main/test.html')

def ajax_posting(request):
    if request.is_ajax():
        user = request.user
        first_name = request.POST.get('first_name', None) # getting data from first_name input
        last_name = request.POST.get('last_name', None)  # getting data from last_name input
        if first_name and last_name: #cheking if first_name and last_name have value
            Url.objects.create(
                full_url=first_name,
                user=user,
            )

            url_hash = Url.objects.get(full_url=first_name).url_hash


            response = {
                         'msg':'Your form has been submitted successfully',
                         'first_name': first_name,
                         'last_name': last_name,
                         'url_hash': '))))))))))))))))',
                         'sperma': 'sperma',
                         'url_hash': url_hash
            }
            return JsonResponse(response) # return response as JSON


