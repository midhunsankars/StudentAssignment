# Generated by Django 3.1.7 on 2021-02-25 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_register_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logintable',
        ),
    ]