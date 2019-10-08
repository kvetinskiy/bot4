import telepot, telebot, time, emoji
from telepot.loop import MessageLoop

bot = telebot.TeleBot('677177030:AAGSZb4ES82-MX2-3VHtAHbny_0KxGTwiiM')
keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard1.row('Цена\U0001F4B5', 'Бизнес\U0001F4B0', 'Контакты\U0000260E')

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Выберите интересующую Вас позицию.', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def handle_text(message):

      if message.text == "Цена\U0001F4B5":
          bot.send_message(message.chat.id, '\U0001F4DDСоздание бота - 10000р\n\U0001F9D4Администрирование - 1000р')

      if message.text == "Бизнес\U0001F4B0":
          bot.send_message(message.chat.id, 'Боты широко используются государственными учреждениями и сетевыми компаниями\nОни существуют для автоматизации и облегчения работы с клиентами\nДля уточнения информации воспользуйтесь разделом "Контакты"')

      if message.text == "Контакты\U0000260E":
          bot.send_message(message.chat.id, 'Наши контакты\n\U0001F4E7E-mail: n.kvetinskiy@gmail.com\n\U00002708Telegram: @kvetinskiy\n\U0001F4F1Мобильный телефон/WhatsApp: +7(705)288-11-22')

bot.polling()
