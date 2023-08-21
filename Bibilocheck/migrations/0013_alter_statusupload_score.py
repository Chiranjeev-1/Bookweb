# Generated by Django 4.2.2 on 2023-06-25 04:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bibilocheck', '0012_alter_statusupload_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusupload',
            name='score',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
