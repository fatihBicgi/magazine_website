# Generated by Django 4.0.1 on 2022-02-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0005_magazine_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]