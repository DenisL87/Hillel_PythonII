# Generated by Django 3.2.9 on 2021-11-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0002_auto_20211107_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
