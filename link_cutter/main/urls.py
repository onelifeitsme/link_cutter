from django.urls import path
from .views import RegisterUserView, LoginUserView, users_urls, get_existing_short_url, Logout, CutView

urlpatterns = [
    path('registration', RegisterUserView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('', CutView.as_view(), name='cut'),
    path('my_urls', users_urls, name='my_urls'),
    path('<str>', get_existing_short_url, name='get_existing_short_url'),
]
