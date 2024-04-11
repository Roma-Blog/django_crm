# Generated by Django 5.0.4 on 2024-04-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
