# Generated by Django 3.2.3 on 2021-06-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_alter_form_myfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='myfile',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
