# Generated by Django 4.2 on 2023-04-28 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]