# Generated by Django 4.2.6 on 2023-10-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_menuitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Изображение'),
        ),
    ]
