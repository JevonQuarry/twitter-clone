# Generated by Django 3.1.6 on 2021-06-23 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20210621_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
