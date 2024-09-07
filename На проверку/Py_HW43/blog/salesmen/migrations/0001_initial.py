# Generated by Django 5.0.7 on 2024-09-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salesmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesman_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('number', models.IntegerField(blank=True, unique=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=50, unique=True, verbose_name='E-mail')),
                ('date', models.DateField(verbose_name='Дата приёма на работу')),
                ('position', models.CharField(choices=[('Продавец', 'Продавец'), ('Старший продавец', 'Старший продавец'), ('Руководитель отдела продаж', 'Руководитель отдела продаж')], default=None, max_length=30, verbose_name='Позиция в фирме')),
            ],
        ),
    ]
