# Generated by Django 4.1.5 on 2023-01-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_details_departure_details_return_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idnum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField()),
            ],
        ),
    ]