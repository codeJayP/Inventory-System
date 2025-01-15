from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('register/', user_register, name="user_register"),
]