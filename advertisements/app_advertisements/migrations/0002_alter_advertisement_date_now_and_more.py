# Generated by Django 4.2.3 on 2023-08-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date_now',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of creation'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Update date'),
        ),
    ]