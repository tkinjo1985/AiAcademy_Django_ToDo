# Generated by Django 3.0.3 on 2020-02-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='done_date',
            field=models.DateTimeField(null=True),
        ),
    ]
