# Generated by Django 5.0.6 on 2024-07-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product.css',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/items/', verbose_name='Изображение'),
        ),
    ]
