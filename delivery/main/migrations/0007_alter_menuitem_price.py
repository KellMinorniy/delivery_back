# Generated by Django 4.2.6 on 2023-10-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_menuitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10, verbose_name='Цена'),
        ),
    ]
