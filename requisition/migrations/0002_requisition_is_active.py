# Generated by Django 4.2.7 on 2024-01-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
