# Generated by Django 4.2.2 on 2023-06-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bibilocheck', '0004_alter_statusupload_completedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusupload',
            name='author',
            field=models.CharField(max_length=1048576, null=True),
        ),
        migrations.AlterField(
            model_name='statusupload',
            name='description',
            field=models.CharField(max_length=1048576, null=True),
        ),
        migrations.AlterField(
            model_name='statusupload',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='statusupload',
            name='note',
            field=models.TextField(max_length=1048576, null=True),
        ),
        migrations.AlterField(
            model_name='statusupload',
            name='title',
            field=models.CharField(max_length=1048576, null=True),
        ),
    ]
