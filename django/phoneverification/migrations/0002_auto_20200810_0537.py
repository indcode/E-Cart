# Generated by Django 2.0 on 2020-08-10 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phoneverification', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='otp',
            new_name='phone_verify',
        ),
    ]
