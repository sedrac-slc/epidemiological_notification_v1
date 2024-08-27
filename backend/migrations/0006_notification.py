# Generated by Django 4.2 on 2024-08-27 14:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_patient_fullnamefather_patient_fullnamemother_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_by', models.UUIDField(blank=True, null=True)),
                ('concat_fields', models.TextField(blank=True, null=True)),
                ('observationDate', models.DateField()),
                ('situation', models.CharField(choices=[('ALIVE', 'ALIVE'), ('DEAD', 'DEAD'), ('STABLE', 'STABLE'), ('CRITICAL', 'CRITICAL'), ('SEVERE', 'SEVERE'), ('IMPROVING', 'IMPROVING'), ('RECOVERED', 'RECOVERED'), ('UNDER_OBSERVATION', 'UNDER_OBSERVATION'), ('REFERRED', 'REFERRED'), ('DISCHARGED', 'DISCHARGED'), ('UNCONSCIOUS', 'UNCONSCIOUS'), ('DECEASED', 'DECEASED')], max_length=100)),
                ('manifestationDate', models.DateField()),
                ('classification', models.CharField(choices=[('CONFIRMED', 'CONFIRMED'), ('SCHEDULED', 'SCHEDULED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'), ('FAILED', 'FAILED'), ('IN_PROGRESS', 'IN_PROGRESS'), ('RESCHEDULED', 'RESCHEDULED'), ('EXPIRED', 'EXPIRED'), ('ON_HOLD', 'ON_HOLD')], max_length=100)),
                ('notificationDate', models.DateField()),
                ('numberOfVaccines', models.IntegerField()),
                ('vaccinationDate', models.DateField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.institution')),
                ('laboratoryTechnician', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.laboratorytechnician')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.patient')),
                ('sickness', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.sickness')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
