# Generated by Django 3.2.8 on 2023-03-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REALESTATE', '0004_alter_realtor_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='lee.jpg', null=True, upload_to=''),
        ),
    ]