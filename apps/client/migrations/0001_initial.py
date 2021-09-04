from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
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
                ('name', models.CharField(max_length=96, verbose_name='Name')),
                (
                    'email',
                    models.EmailField(
                        max_length=96, unique=True, verbose_name='E-mail'
                    ),
                ),
                (
                    'created',
                    models.DateTimeField(auto_now_add=True, verbose_name='Created'),
                ),
                (
                    'products',
                    models.ManyToManyField(
                        blank=True, to='product.Product', verbose_name='Product'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'client',
            },
        ),
    ]
