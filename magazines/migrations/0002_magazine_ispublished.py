# Generated by Django 4.0.1 on 2022-02-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
    ]
