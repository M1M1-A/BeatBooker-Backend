# Generated by Django 4.2.5 on 2023-09-20 14:15

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
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
            ],
        ),
    ]