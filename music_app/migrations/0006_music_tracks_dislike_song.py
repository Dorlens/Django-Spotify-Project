# Generated by Django 5.1.6 on 2025-02-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0005_rename_uservote_music_tracks_like_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='music_tracks',
            name='dislike_song',
            field=models.BooleanField(default=False),
        ),
    ]
