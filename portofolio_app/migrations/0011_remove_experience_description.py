# Generated by Django 5.0.6 on 2024-10-04 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio_app', '0010_generalskill_icon_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='description',
        ),
    ]
