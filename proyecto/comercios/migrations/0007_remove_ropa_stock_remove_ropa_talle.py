# Generated by Django 5.1 on 2024-09-07 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercios', '0006_alter_talle_talle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ropa',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='ropa',
            name='talle',
        ),
    ]
