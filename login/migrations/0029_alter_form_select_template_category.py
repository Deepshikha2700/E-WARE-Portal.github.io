# Generated by Django 3.2.3 on 2021-06-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0028_alter_form_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Select_Template_Category',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
