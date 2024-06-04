# Generated by Django 5.0.6 on 2024-06-01 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_institution_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipal',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.province'),
        ),
    ]
