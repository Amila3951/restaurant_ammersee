# Generated by Django 4.2.16 on 2025-01-10 14:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import restaurant.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.CharField(default='Main Courses', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('num_people', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator()])),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?\\d{9,15}$')])),
                ('date', models.DateField(validators=[restaurant.models.validate_future_date])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
