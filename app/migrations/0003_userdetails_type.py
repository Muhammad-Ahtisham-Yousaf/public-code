# Generated by Django 5.0 on 2024-02-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='type',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
