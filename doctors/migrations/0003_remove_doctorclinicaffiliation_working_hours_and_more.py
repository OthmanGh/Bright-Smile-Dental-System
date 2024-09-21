# Generated by Django 5.1.1 on 2024-09-20 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_remove_doctor_specialties_delete_specialty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorclinicaffiliation',
            name='working_hours',
        ),
        migrations.AddField(
            model_name='doctorclinicaffiliation',
            name='end_time',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
        migrations.AddField(
            model_name='doctorclinicaffiliation',
            name='start_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AlterField(
            model_name='doctorclinicaffiliation',
            name='working_days',
            field=models.CharField(blank=True, choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=50),
        ),
    ]
