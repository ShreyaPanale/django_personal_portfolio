# Generated by Django 2.2.6 on 2020-07-13 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20200712_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='title',
        ),
    ]
