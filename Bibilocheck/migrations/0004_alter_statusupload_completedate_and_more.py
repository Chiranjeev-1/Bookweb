# Generated by Django 4.2.2 on 2023-06-24 07:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bibilocheck', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusupload',
            name='completedate',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='statusupload',
            name='startdate',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
