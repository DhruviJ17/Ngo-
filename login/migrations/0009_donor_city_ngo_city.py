# Generated by Django 4.0.4 on 2022-04-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20200927_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
