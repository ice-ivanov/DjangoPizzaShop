# Generated by Django 2.0 on 2019-09-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True, verbose_name='Date')),
                ('weekday', models.CharField(choices=[('6', 'Saturday'), ('3', 'Wednesday'), ('2', 'Tuesday'), ('7', 'Sunday'), ('4', 'Thursday'), ('5', 'Friday'), ('1', 'Monday')], max_length=1, verbose_name='Day of the week')),
                ('is_active', models.BooleanField(default=False, verbose_name='Working')),
                ('message', models.TextField(blank=True, max_length=225, null=True, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Date',
                'verbose_name_plural': 'Dates',
            },
        ),
    ]