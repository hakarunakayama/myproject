# Generated by Django 4.1.7 on 2024-01-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]