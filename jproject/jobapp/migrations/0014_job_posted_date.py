# Generated by Django 5.0.6 on 2024-06-25 17:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0013_remove_job_posted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='posted_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
