# Generated by Django 3.0.9 on 2020-08-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0041_auto_20200810_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitch_login',
            field=models.CharField(editable=False, max_length=25, null=True),
        ),
    ]