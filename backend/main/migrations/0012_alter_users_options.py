# Generated by Django 4.2.5 on 2023-10-08 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Organisation Users'},
        ),
    ]