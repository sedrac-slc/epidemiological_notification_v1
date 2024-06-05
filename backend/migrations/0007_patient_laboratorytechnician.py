# Generated by Django 4.2 on 2024-06-05 08:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_municipal_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.UUIDField(blank=True, null=True)),
                ('concat_fields', models.TextField(unique=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LaboratoryTechnician',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.UUIDField(blank=True, null=True)),
                ('concat_fields', models.TextField(unique=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
