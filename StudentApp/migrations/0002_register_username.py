# Generated by Django 3.1.7 on 2021-02-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default=11, max_length=200),
            preserve_default=False,
        ),
    ]
