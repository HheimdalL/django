# Generated by Django 4.1.3 on 2022-11-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_day',
            field=models.DateField(auto_now_add=True),
        ),
    ]