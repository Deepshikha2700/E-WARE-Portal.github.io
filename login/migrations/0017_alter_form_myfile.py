# Generated by Django 3.2.3 on 2021-06-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_rename_timestamp_profile_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='myfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
