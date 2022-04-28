# Generated by Django 3.1.1 on 2020-09-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_remove_ngo_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='state',
        ),
        migrations.AddField(
            model_name='ngo',
            name='logo',
            field=models.ImageField(blank=True, default='ngo.jpg', null=True, upload_to=''),
        ),
    ]