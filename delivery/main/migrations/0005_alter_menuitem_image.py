# Generated by Django 4.2.6 on 2023-10-11 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Изображение'),
        ),
    ]
