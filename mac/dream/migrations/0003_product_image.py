# Generated by Django 3.1.7 on 2021-03-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream', '0002_auto_20210330_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=' ', upload_to='dream/images'),
        ),
    ]