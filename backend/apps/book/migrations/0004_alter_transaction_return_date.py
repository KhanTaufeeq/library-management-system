# Generated by Django 5.1.4 on 2025-01-09 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_book_id_transaction_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='return_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Return Date'),
        ),
    ]