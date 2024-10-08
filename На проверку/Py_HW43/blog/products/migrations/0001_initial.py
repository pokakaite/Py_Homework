# Generated by Django 5.0.7 on 2024-09-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=150, verbose_name='Описание')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
            ],
        ),
    ]
