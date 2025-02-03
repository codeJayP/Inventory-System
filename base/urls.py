from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_page, name="home"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('register/', user_register, name="user_register"),
    path('employee_page/', employee_page, name="employee_page"),
    path('item_list/', item_list, name="item_list"),
    path('add_item/', add_item, name="add_item"),
    path('edit_item/<int:pk>/', edit_item, name="edit_item"),

    path('user_list/', user_list, name="user_list"),
    path('equipment_pdf/<int:pk>/', equipment_pdf, name="equipment_pdf"),
    path('generate_repair_request_pdf/', generate_repair_request_pdf, name="generate_repair_request_pdf"),
]