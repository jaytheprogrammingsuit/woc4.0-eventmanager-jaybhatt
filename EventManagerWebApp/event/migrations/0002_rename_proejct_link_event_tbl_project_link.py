# Generated by Django 4.0.1 on 2022-01-19 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_tbl',
            old_name='proejct_link',
            new_name='project_link',
        ),
    ]
