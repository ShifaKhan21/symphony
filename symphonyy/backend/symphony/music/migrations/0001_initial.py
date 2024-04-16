# Generated by Django 5.0.3 on 2024-04-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('albums_sold', models.IntegerField()),
                ('active_since', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BrowseAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='browse_all_images/')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('duration', models.DurationField()),
                ('url', models.URLField()),
            ],
        ),
    ]