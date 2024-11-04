from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100,choices=(
        ('HR', 'Human Resources'),
        ('Engineering', 'Engineering'),
        ('Sales', 'Sales'),
    ))
    role = models.CharField(max_length=100,choices=(
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Analyst', 'Analyst'),
    ))
    date_joined = models.DateField(auto_now_add=True)