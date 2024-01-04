# Generated by Django 5.0.1 on 2024-01-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='place')),
            ],
        ),
    ]
