# Generated by Django 3.0 on 2019-12-14 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191214_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='clients',
        ),
    ]
