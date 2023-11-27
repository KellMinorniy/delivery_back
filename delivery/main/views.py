from django.shortcuts import render
from .models import MenuItem
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum, F
from .telegram_bot import send_order_to_telegram



def index(request):
    context = {}
    for t in MenuItem.TYPE:
        context[f'menu_{t[0]}'] = MenuItem.objects.filter(type__exact=t[0])

    cart, created = Cart.objects.get_or_create()
    cart_items = CartItem.objects.filter(cart=cart)
    context['cart_items'] = cart_items
    context['cart'] = cart

    return render(request, 'main/index.html', context)



def add_to_cart(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    cart, created = Cart.objects.get_or_create()
    cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
    if not created:
        cart_item.update_quantity(cart_item.quantity + 1)
    return redirect('cart')



def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart).annotate(total_price=F('menu_item__price'))
    for item in cart_items:
        print(f"Total price for item {item.id}: {item.total_price}")
    cart_items = cart_items.aggregate(total_cart=Sum('total_price'))
    total_cart = total_cart['total_cart'] if total_cart else 0
    return render(request, 'main/index.html', {'cart_items': cart_items, 'total_cart': total_cart})



def remove_from_cart(request, menu_item_id):
    cart_items = CartItem.objects.filter(menu_item_id=menu_item_id)
    for item in cart_items:
        item.delete()
    return redirect('cart')


def order(request):
    cart, created = Cart.objects.get_or_create()
    cart_items = CartItem.objects.filter(cart=cart)
    context = {'cart_items': cart_items, 'cart': cart}
    return render(request, 'main/order.html', context)




import telebot

bot = telebot.TeleBot('6666643875:AAH9RejQrz5iw8YwP7A5mtfmrJ71CAnsTEQ')

def submit_order(request):
    if request.method == 'POST':
        # Получите данные формы
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        adress = request.POST.get('adress', '')
        comment = request.POST.get('comment', '')
        payment = request.POST.get('payment', '')
        items = request.POST.getlist('items')
        prices = request.POST.getlist('prices')
        total_price = request.POST.get('total_price', '')

        # Соберите данные заказа в словарь
        order_data = {
            'name': name,
            'phone': phone,
            'adress': adress,
            'comment': comment,
            'payment': payment,
            'items': items,
            'prices': prices,
            'total_price': total_price,
        }

        # Создайте сообщение
        message = f"Новый заказ!\nИмя: {order_data['name']}\nТелефон: {order_data['phone']}\nАдрес доставки: {order_data['adress']}\nКоментарий: {order_data['comment']}\nСпособ оплаты: {order_data['payment']}\nБлюда: {', '.join(order_data['items'])}\nЦены: {', '.join(order_data['prices'])}\nОбщая стоимость: {order_data['total_price']}\n"

        # Отправьте сообщение в канал Telegram
        bot.send_message(chat_id='-1001900895811', text=message)

        return redirect('finish')  # перенаправление обратно на страницу заказа после обработки заказа
    else:
        return redirect('order')


def finish(request):
    return render(request, 'main/finish.html')




