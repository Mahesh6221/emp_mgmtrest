# Generated by Django 5.1.1 on 2024-11-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]