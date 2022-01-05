from django.urls import path
from .views import RegisterUserView, LoginUserView, users_urls, get_existing_short_url, ajax_posting, cutview, Logout

urlpatterns = [
    path('registration', RegisterUserView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('', cutview, name='cut'),
    path('ajax-posting/', ajax_posting, name='ajax_posting'),
    path('my_urls', users_urls, name='my_urls'),
    path('<str>', get_existing_short_url, name='get_existing_short_url'),
]

