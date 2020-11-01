# Generated by Django 3.1.1 on 2020-10-31 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_promocode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocode',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.promocode'),
        ),
    ]