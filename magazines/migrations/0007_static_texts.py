# Generated by Django 4.0.1 on 2022-02-10 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0006_alter_magazine_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Static_Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(default='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]