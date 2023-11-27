import telebot

def send_order_to_telegram(order_data):
    # Создайте сообщение
    message = f"Новый заказ!\nИмя: {order_data['name']}\nТелефон: {order_data['phone']}\nАдрес доставки: {order_data['adress']}\nКоментарий: {order_data['comment']}\nСпособ оплаты: {order_data['payment']}\nНазвание блюда: {order_data['item']}\nЦена: {order_data['price']}\nОбщая стоимость: {order_data['total_price']}\n"

    # Отправьте сообщение в канал Telegram
    bot = telebot.TeleBot('6666643875:AAH9RejQrz5iw8YwP7A5mtfmrJ71CAnsTEQ')
    bot.send_message(chat_id='-1001900895811', text=message)
