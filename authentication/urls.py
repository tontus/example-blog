from django.urls import path
from authentication.views import user_login, register

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register),
]
