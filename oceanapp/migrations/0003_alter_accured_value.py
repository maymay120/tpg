# Generated by Django 4.0.3 on 2022-04-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oceanapp', '0002_alter_profile_file_alter_profile_file2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accured',
            name='value',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]