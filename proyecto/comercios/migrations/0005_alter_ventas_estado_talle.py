# Generated by Django 5.1 on 2024-09-07 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercios', '0004_alter_cliente_options_alter_ropa_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('EN_PROCESOEn Proceso', 'En Proceso'), ('COMPLETADO', 'Completado'), ('CANCELADO', 'Cancelado')], default='PENDIENTE', max_length=20),
        ),
        migrations.CreateModel(
            name='Talle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(max_length=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('ropa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talles', to='comercios.ropa')),
            ],
            options={
                'verbose_name': 'Talle',
                'verbose_name_plural': 'Talles',
            },
        ),
    ]
