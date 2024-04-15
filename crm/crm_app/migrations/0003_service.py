# Generated by Django 5.0.4 on 2024-04-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0002_master_client_comments_alter_client_birthday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
        ),
    ]
