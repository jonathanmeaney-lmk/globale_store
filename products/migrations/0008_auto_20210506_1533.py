# Generated by Django 3.1.7 on 2021-05-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210426_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.PositiveIntegerField(),
        ),
    ]
