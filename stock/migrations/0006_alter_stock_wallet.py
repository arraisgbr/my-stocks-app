# Generated by Django 4.2.5 on 2023-10-01 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
        ('stock', '0005_alter_stock_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wallet.wallet'),
        ),
    ]