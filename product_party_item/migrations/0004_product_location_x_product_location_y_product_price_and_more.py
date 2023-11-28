# Generated by Django 4.0.3 on 2023-11-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_party_item', '0003_remove_productimage_product_image_productimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location_x',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location_y',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]