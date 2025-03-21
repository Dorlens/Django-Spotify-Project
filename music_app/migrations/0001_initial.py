# Generated by Django 5.1.6 on 2025-02-25 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music_tracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_title', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=100)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('Audio_file', models.URLField()),
                ('cover_image', models.URLField()),
            ],
        ),
    ]
