# Generated by Django 2.1.7 on 2019-04-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20190331_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='average_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
