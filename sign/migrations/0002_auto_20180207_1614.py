# Generated by Django 2.0.2 on 2018-02-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='signature',
            field=models.CharField(max_length=65536),
        ),
    ]
