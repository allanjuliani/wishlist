# Generated by Django 4.0.2 on 2022-02-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True, verbose_name='Updated at'
            ),
        ),
    ]
