# Generated by Django 3.2.3 on 2021-06-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_alter_form_myfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='myfile',
            field=models.FileField(upload_to='media/%Y/%m/%d/'),
        ),
    ]
