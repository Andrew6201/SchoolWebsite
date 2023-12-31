# Generated by Django 4.2.4 on 2023-11-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('programme', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('nationality', models.CharField(max_length=500)),
                ('age', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=500)),
            ],
        ),
    ]
