# Generated by Django 4.2.16 on 2024-11-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_reservation_delete_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='last_name',
        ),
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]