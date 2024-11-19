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
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',  
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(validators=[restaurant.models.validate_future_date])), 
                ('time', models.TimeField()),
                ('num_people', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?\\d{9,15}$')])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]