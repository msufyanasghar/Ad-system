# Generated by Django 4.2.7 on 2023-11-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='daily_visitor_limit',
            field=models.IntegerField(default=0),
        ),
    ]