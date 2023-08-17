# Generated by Django 3.2 on 2023-08-14 13:20

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20230812_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Био'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+\\Z', 'В никнейме допустимы только цифры, буквы и символы @/./+/-/_'), users.validators.validate_username], verbose_name='Никнейм'),
        ),
    ]