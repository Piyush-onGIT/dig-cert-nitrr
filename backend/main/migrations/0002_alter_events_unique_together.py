# Generated by Django 4.2.5 on 2023-10-05 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='events',
            unique_together={('organisation', 'event_data')},
        ),
    ]
