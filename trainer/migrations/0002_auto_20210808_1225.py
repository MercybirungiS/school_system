# Generated by Django 3.2.5 on 2021-08-08 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='joining_date',
        ),
    ]
