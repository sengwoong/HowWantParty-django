# Generated by Django 4.0.3 on 2023-11-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_party_item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product_image',
            field=models.CharField(max_length=100),
        ),
    ]