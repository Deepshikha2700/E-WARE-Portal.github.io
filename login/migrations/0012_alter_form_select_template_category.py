# Generated by Django 3.2.3 on 2021-06-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20210621_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Select_Template_Category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
