# Generated by Django 4.2.6 on 2023-12-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='Topic_name',
            field=models.CharField(max_length=100),
        ),
    ]
