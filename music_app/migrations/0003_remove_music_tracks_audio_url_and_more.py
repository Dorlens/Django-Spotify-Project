# Generated by Django 5.1.6 on 2025-02-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_rename_artist_name_music_tracks_artist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music_tracks',
            name='audio_url',
        ),
        migrations.AddField(
            model_name='music_tracks',
            name='preview_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
