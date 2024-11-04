
import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department', lookup_expr='iexact')  
    role = django_filters.CharFilter(field_name='role', lookup_expr='iexact') 

    class Meta:
        model = Employee
        fields = ['department', 'role']