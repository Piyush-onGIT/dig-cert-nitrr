# Generated by Django 4.2.5 on 2023-10-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_faculty_org_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='isCDC',
            field=models.BooleanField(default=True),
        ),
    ]