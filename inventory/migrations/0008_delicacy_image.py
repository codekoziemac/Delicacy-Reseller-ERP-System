# Generated by Django 4.2.7 on 2024-01-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_variation_reorder_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='delicacy',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]