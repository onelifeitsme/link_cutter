from django.urls import path
from .views import home, RegisterUserView, LoginUserView, users_urls, CutView, get_existing_short_url, test, cutviewajax, cutview, AuthorCreate, ajax_posting

urlpatterns = [
    path('', home, name='home'),
    path('registration', RegisterUserView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('cut', AuthorCreate.as_view(), name='cut'),
    path('test', test, name='usertest'),
    path('my_urls', users_urls, name='my_urls'),
    path('<str>', get_existing_short_url, name='get_existing_short_url'),
    path('ajax-posting/', ajax_posting, name='ajax_posting'),
]

