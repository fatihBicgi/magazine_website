# Generated by Django 4.0.1 on 2022-02-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0004_alter_magazine_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
