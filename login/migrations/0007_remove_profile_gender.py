# Generated by Django 3.2.3 on 2021-06-05 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]
