# Generated by Django 4.0.3 on 2022-05-20 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oceanapp', '0022_alter_profile_back_alter_profile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='num_refer',
            field=models.IntegerField(default=0),
        ),
    ]
