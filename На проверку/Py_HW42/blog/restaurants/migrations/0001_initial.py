# Generated by Django 5.1 on 2024-08-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('cuisine', models.CharField(max_length=50, verbose_name='Кухня')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('web_site', models.CharField(max_length=100, verbose_name='Веб-сайт')),
                ('contacts', models.IntegerField(verbose_name='Номер телефона')),
            ],
        ),
    ]
