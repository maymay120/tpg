# Generated by Django 4.0.3 on 2022-04-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oceanapp', '0003_alter_accured_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accured',
            name='value',
            field=models.CharField(blank=True, default=0, max_length=20000, null=True),
        ),
    ]
