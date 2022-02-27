# Generated by Django 4.0.2 on 2022-02-27 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Created at'
                    ),
                ),
                (
                    'updated_at',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Updated at'
                    ),
                ),
                (
                    'client',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='client.client',
                        verbose_name='',
                    ),
                ),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='product.product',
                        verbose_name='',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Favorite',
                'verbose_name_plural': 'Favorites',
            },
        ),
    ]
