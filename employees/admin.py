from django.contrib import admin
from .models import *

# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ('name','email',)
    list_filter = ('department',)



admin.site.register(Employee,EmpAdmin)

# mahesh
# mahesh@gmail.com
# 123