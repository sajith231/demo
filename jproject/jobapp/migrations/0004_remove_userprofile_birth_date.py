# Generated by Django 5.0.6 on 2024-06-23 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_candidate_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth_date',
        ),
    ]