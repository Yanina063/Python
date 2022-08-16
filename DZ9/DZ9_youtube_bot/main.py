import telebot
from telebot import types

bot = telebot.TeleBot('5557829847:AAGXRI-PV8rHXpHeSj2eD77aC1rIKv8L7lE')


# Отслеживание команд
@bot.message_handler(commands=['start'])
def start(message):  # сообщение от пользователя
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Посмотрите видео на youtube", url="https://www.youtube.com/watch?v=HodO2eBEz_8"))
    bot.send_message(message.chat.id, 'Посмотрите видео', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Рад тебе!", parse_mode='html')
    elif message.text == 'photo':
        photo = open('youtube.png', 'rb')  # открыть картинку, указываем картинку и команду
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Введи пожалуйста команду", parse_mode='html')


bot.polling(non_stop=True)  # Запускаем наш бот на постоянную обработку, бесконечный цикл
