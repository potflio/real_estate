# Generated by Django 5.0.4 on 2024-06-24 19:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landresale',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
