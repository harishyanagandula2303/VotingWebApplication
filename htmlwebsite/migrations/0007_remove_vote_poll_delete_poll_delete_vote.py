# Generated by Django 5.0.3 on 2024-04-01 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0006_poll_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
