# Generated by Django 4.2.21 on 2025-05-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifas', '0002_rifa_cuenta_rifa_numerocuenta_rifa_qr'),
    ]

    operations = [
        migrations.AddField(
            model_name='rifa',
            name='numeroasesor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
