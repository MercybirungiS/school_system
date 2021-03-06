# Generated by Django 3.2.5 on 2021-08-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, default='DEFAULT VALUE', max_length=12, null=True)),
                ('event_description', models.TextField(blank=True, null=True)),
                ('event_duration', models.TimeField(blank=True, null=True)),
                ('event_agenda', models.CharField(blank=True, max_length=200, null=True)),
                ('event_venue', models.CharField(blank=True, max_length=15, null=True)),
                ('event_organiser', models.CharField(blank=True, max_length=12, null=True)),
                ('event_link', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]
