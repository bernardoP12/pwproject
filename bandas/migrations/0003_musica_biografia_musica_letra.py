# Generated by Django 4.0.6 on 2024-06-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_banda_rename_song_musica_rename_year_album_ano_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='biografia',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='letra',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]