# Generated by Django 5.1.2 on 2024-11-17 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmStoreApp', '0002_remove_carrito_cantidad_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carritos_kmstore', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ordenenvio',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_kmstore', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
    ]
