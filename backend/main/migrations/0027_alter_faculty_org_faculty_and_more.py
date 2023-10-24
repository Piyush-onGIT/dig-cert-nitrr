# Generated by Django 4.2.5 on 2023-10-24 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_faculty_org_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_org',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.faculty_advisor', to_field='email'),
        ),
        migrations.AlterField(
            model_name='faculty_org',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.organisation', to_field='name'),
        ),
    ]
