# Generated by Django 3.2.3 on 2021-06-29 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0034_rename_form_phising'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phising',
            new_name='Phishing',
        ),
    ]
