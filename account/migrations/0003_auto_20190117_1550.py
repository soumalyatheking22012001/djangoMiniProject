# Generated by Django 2.0.10 on 2019-01-17 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190117_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfile',
            options={'ordering': ['name'], 'verbose_name': 'userfile'},
        ),
    ]
