# Generated by Django 4.0.1 on 2022-01-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_rename_project_link_event_tbl_poster_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_tbl',
            name='poster_link',
            field=models.URLField(),
        ),
    ]
