from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_page, name="home"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('register/', user_register, name="user_register"),
    path('employee_page/', employee_page, name="employee_page"),
    path('item_list/', item_list, name="item_list"),
]