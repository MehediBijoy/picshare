# Generated by Django 3.0.5 on 2020-04-27 03:45

import UserApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='defaultProfilePic.jpg', upload_to=UserApp.models.upload_to_profile_pic),
        ),
    ]