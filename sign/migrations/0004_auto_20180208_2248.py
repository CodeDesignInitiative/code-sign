# Generated by Django 2.0.2 on 2018-02-08 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0003_signature_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signature',
            old_name='date',
            new_name='timestamp',
        ),
    ]
