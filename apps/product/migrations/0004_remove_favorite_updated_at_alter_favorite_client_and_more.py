# Generated by Django 4.0.2 on 2022-02-27 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('product', '0003_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='client',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='client.client',
                verbose_name='Client',
            ),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='product.product',
                verbose_name='Product',
            ),
        ),
    ]
