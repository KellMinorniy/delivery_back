from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def get_total_price(self):
        total = sum(Decimal(item.menu_item.price) * item.quantity for item in self.items.all())
        return total if total else 0

class CartItem(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', related_name='items', on_delete=models.CASCADE)
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        self.save()



class MenuItem(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='images')
    title = models.CharField(max_length=80, verbose_name='Название')
    weight = models.CharField(max_length=15, verbose_name='Вес')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    description = models.TextField(max_length=120, default=0, verbose_name='Состав')

    TYPE = [
        ('eat', 'Закуски'),
        ('soup', 'Супы'),
        ('pizza', 'Пицца'),
        ('pasta', 'Паста'),
        ('sandwitch', 'Сэндвичи'),
        ('hot', 'Горячие блюда'),
        ('desert', 'Десерты'),
        ('drinks', 'Напитки'),
        ('sous', 'Соусы'),
        ('salat', 'Салаты')
    ]

    type = models.CharField(choices=TYPE, max_length=15, default='eat', verbose_name='Категория')

    def __str__(self):
        return self.title
    

