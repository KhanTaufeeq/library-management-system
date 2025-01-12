# Generated by Django 5.1.4 on 2025-01-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('author', models.CharField(max_length=30, verbose_name='Author')),
                ('publication_year', models.DateField(verbose_name='Publication Year')),
                ('availability_status', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
    ]
