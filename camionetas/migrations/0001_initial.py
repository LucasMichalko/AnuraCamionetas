# Generated by Django 3.2.19 on 2024-09-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='camioneta_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rulo', models.FloatField()),
                ('base_t19', models.FloatField()),
                ('tubo_t19', models.FloatField()),
            ],
        ),
    ]