from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
   path('employees/', GetAllEmployees, name='get_all_employees'),
   path('employees/<int:id>/', getSingleEmployee, name='get_single_employee'),
   path('employees/create/', post_Employee, name='create_employee'),
   path('employees/update/<int:id>/', update_Employee, name='update_employee'),
   path('employees/delete/<int:id>/', delete_Employee, name='delete_employee'),
]