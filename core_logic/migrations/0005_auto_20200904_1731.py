# Generated by Django 3.1 on 2020-09-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_logic', '0004_auto_20200904_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extend',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='income',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
