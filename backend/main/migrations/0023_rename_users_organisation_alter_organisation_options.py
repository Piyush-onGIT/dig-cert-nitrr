# Generated by Django 4.2.5 on 2023-10-20 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_faculty_org_faculty_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Organisation',
        ),
        migrations.AlterModelOptions(
            name='organisation',
            options={'verbose_name_plural': 'Organisations'},
        ),
    ]
