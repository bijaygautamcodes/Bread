# Generated by Django 4.0.2 on 2022-02-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0008_rename_order_name_delivery_remarks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='remarks',
            field=models.CharField(default=None, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='token',
            field=models.CharField(default='7ZA73F', max_length=6),
        ),
    ]