# Generated by Django 3.2.8 on 2023-08-26 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('REALESTATE', '0008_auto_20230826_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='county',
            new_name='location',
        ),
    ]