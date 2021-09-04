from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Product',
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
                    'title',
                    models.CharField(max_length=255, unique=True, verbose_name='Title'),
                ),
                (
                    'slug',
                    models.SlugField(
                        max_length=255, null=True, unique=True, verbose_name='Slug'
                    ),
                ),
                (
                    'price',
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name='Price'
                    ),
                ),
                ('image', models.URLField(verbose_name='Image')),
                (
                    'brand',
                    models.CharField(
                        db_index=True, max_length=96, verbose_name='Brand'
                    ),
                ),
                (
                    'review_score',
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (1, '⭐'),
                            (2, '⭐⭐'),
                            (3, '⭐⭐⭐'),
                            (4, '⭐⭐⭐⭐'),
                            (5, '⭐⭐⭐⭐⭐'),
                        ],
                        null=True,
                        verbose_name='Review Score',
                    ),
                ),
                (
                    'created',
                    models.DateTimeField(auto_now_add=True, verbose_name='Created'),
                ),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
    ]
