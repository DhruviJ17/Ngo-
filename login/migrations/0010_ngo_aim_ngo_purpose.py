# Generated by Django 4.0.4 on 2022-05-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_donor_city_ngo_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='aim',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
    ]
