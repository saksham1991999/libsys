# Generated by Django 2.2 on 2020-01-28 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='max_price_range',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='min_price_range',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='non_refundable_charges',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
