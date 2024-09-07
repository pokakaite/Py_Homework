# Generated by Django 5.0.7 on 2024-09-07 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('salesmen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=bool, verbose_name='Оформлено?')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
                ('salesman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesmen.salesmen')),
            ],
        ),
    ]
