# Generated by Django 5.0.6 on 2024-06-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_userprofile_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]