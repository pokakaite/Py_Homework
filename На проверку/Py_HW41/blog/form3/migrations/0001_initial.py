# Generated by Django 5.0.7 on 2024-08-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский'), ('Н', 'Неважно')], default=None, max_length=10)),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('agreement', models.Field()),
            ],
        ),
    ]
