# Generated by Django 2.2 on 2021-04-29 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='titile',
            new_name='title',
        ),
    ]