# Generated by Django 2.1.7 on 2019-02-23 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
