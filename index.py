import telepot, time, subprocess, telebot, datetime
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if '/start' in command:
            p = "Привет! Чтобы узнать возможности бота\nнапиши /help"
            bot.sendMessage(chat_id, p)

        if  '/help' in command:
            p = "Помощь\nНаши продукты  - /price \nНаши контакты - /info \nИспользование телеграм ботов в бизнесе - /buis"
            bot.sendMessage(chat_id, p)

        if  '/price' in command:#В кавычках команда которую мы будем писать в телеграмм.
                            #Можно и слова и по русски но начинать нужно именно с косой палочки
            p = "Создание бота - 10000р\nАдминистрирование - 1000р"#А тут собственно выполняется команда которую
                            #мы задали для переменной "cmd0"
            bot.sendMessage(chat_id, p)#А это ответ бота в чат.

        if  '/info' in command:
            p = "Наши контакты\nE-mail: n.kvetinskiy@gmail.com\nTelegram: @kvetinskiy\nМобильный телефон/WhatsApp: +7(705)288-11-22"
            bot.sendMessage(chat_id, p)

        if  '/buis' in command:
            p = "Боты широко используются сетевыми компаниями и государственными учреждениями\nОни существуют для облегчения и автоматизации работы с большим потоком клиентов\nНаши администраторы и программисты очень постараются для вашего удобства и исправной работой ваших ботов\nДля просмотра наших контактов напишите /info"
            bot.sendMessage(chat_id, p)



bot = telepot.Bot('677177030:AAGSZb4ES82-MX2-3VHtAHbny_0KxGTwiiM')#Вместо иксов пишем ваш токен
bot.message_loop(handle)

while 1:
    time.sleep(20)

bot.polling()
