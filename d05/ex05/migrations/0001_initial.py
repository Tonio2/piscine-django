# Generated by Django 5.0.1 on 2024-01-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('episode_nb', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('opening_crawl', models.TextField()),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
