import telepot, telebot, time
from telepot.loop import MessageLoop

bot = telebot.TeleBot('677177030:AAGSZb4ES82-MX2-3VHtAHbny_0KxGTwiiM')
keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard1.row('/Цена', '/Бизнес', '/Контакты')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Выберите интересующую Вас позицию.', reply_markup=keyboard1)

@bot.message_handler(commands=['Цена'])
def start_message(message):
    bot.send_message(message.chat.id, 'Создание бота - 10000р\nАдминистрирование - 1000р')

@bot.message_handler(commands=['Бизнес'])
def start_message(message):
    bot.send_message(message.chat.id, 'Боты широко используются государственными учреждениями и сетевыми компаниями\nОни существуют для автоматизации и облегчения работы с клиентами\nДля уточнения информации воспользуйтесь разделом "Контакты"')

@bot.message_handler(commands=['Контакты'])
def start_message(message):
    bot.send_message(message.chat.id, 'Наши контакты\nE-mail: n.kvetinskiy@gmail.com\nTelegram: @kvetinskiy\nМобильный телефон/WhatsApp: +7(705)288-11-22')

bot.polling()
