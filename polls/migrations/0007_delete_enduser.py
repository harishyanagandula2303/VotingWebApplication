# Generated by Django 5.0.3 on 2024-04-04 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_enduser_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EndUser',
        ),
    ]
