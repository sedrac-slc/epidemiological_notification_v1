# Generated by Django 5.0.6 on 2024-08-07 20:36

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.UUIDField(blank=True, null=True)),
                ('concat_fields', models.TextField(blank=True, null=True)),
                ('name', models.TextField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.UUIDField(blank=True, null=True)),
                ('concat_fields', models.TextField(blank=True, null=True)),
                ('name', models.TextField(max_length=255)),
                ('nunicipality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.municipality')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.UUIDField(blank=True, null=True)),
                ('concat_fields', models.TextField(blank=True, null=True)),
                ('name', models.TextField(max_length=255)),
                ('type', models.CharField(choices=[('PRINCIPAL', 'PRINCIPAL'), ('ALTERNATIVE', 'ALTERNATIVE'), ('WHATSAPP', 'WHATSAPP')], max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
