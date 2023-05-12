# Generated by Django 4.2.1 on 2023-05-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=20, unique=True)),
                ('vehicle_type', models.CharField(choices=[('2', 'Two Wheeler'), ('3', 'Three Wheeler'), ('4', 'Four Wheeler')], max_length=1)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('vehicle_description', models.TextField()),
            ],
        ),
    ]
