# Generated by Django 5.1.1 on 2024-09-04 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_articles_transport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='transport',
            new_name='Predmet',
        ),
    ]
