# Generated by Django 2.2 on 2022-05-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]
