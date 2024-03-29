# Generated by Django 4.0.2 on 2022-02-27 21:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'product',
            '0004_remove_favorite_updated_at_alter_favorite_client_and_more',
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name='Created at',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='Updated at'
            ),
        ),
    ]
