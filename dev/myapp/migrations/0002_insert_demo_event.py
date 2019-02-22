# Generated by Django 2.1 on 2018-08-26 18:54

from django.db import migrations
from datetime import datetime
import pytz


def insert_demo_event(apps, schema_editor):
    event_datetime = datetime(2019, 2, 4, 0, 0, tzinfo=pytz.UTC)

    event = apps.get_model('myapp', 'Event')()
    event.name = 'Event 01'
    event.start_date = datetime.date(event_datetime)
    event.end_date = datetime.date(event_datetime)
    event.start_time = datetime.time(event_datetime)
    event.end_time = datetime.time(event_datetime)
    event.start_datetime = event_datetime
    event.end_datetime = event_datetime
    event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_demo_event),
    ]
