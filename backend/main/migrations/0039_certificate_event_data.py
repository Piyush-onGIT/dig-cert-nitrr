# Generated by Django 4.2.5 on 2024-02-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_rename_certificate_path_certificate_cdc_signature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='event_data',
            field=models.CharField(default='nu'),
            preserve_default=False,
        ),
    ]
