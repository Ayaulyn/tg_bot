import telebot
import requests
import webbrowser
import json
from telebot import types

bot = telebot.TeleBot('6937544265:AAFUmvDKLY9NawVkHDC8LU9Rk19Qy0YYP4s')
API='70b8980921062092317bff523be8da7a'


@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id,'⛅')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Расскажи мне о сегодняшний погоде ☀️', callback_data='weather'))
    markup.add(types.InlineKeyboardButton('Я турист🤳🏛️!', callback_data='tourist'))
    markup.add(types.InlineKeyboardButton('Милые котики 💞💗💓!', callback_data='cats'))

    bot.register_next_step_handler(message, on_click)
    bot.send_message(message.chat.id,
                     f'Хэй! Я Weather bot! 😶‍🌫.\n'
                     f'Моя миссия уведомлять вас о погоде а также, помощь с ознакомлением города, если вы турист. 🧳 \n'
    f'Я могу🦾:\n' 
f'1) Рассказать тебе о сегодняшний погоде ☀️ \n'

f'2) Ознакомить с городом,если ты турист 🏛️ \n'


f'3) Показать мемы про кошек💗,\n'
                    ,reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

@bot.callback_query_handler(func=lambda call: True)
def on_click(call):
    if call.data == 'weather':
        bot.send_message(call.message.chat.id, 'Напишите название города:)')

    elif call.data == 'tourist':
        bot.send_message(call.message.chat.id, 'Лучшие заведения города...')
    elif call.data == 'cats':
        bot.send_message(call.message.chat.id, 'Все будет - потерпите немножко')




@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message,f'Отлично! Погода сейчас:{data["main"]["temp"]}'f'градуса')








@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Купить мне такую',url='https://mercedes-benz-astana.kz/'))
    markup.add(types.InlineKeyboardButton('Я бомж', url = 'https://smailiki.ucoz.net/_ph/14/2/6007173.jpg'))
    bot.reply_to(message, 'Охх,соска', reply_markup=markup)


@bot.message_handler(commands=['moodle'])
def site(message):
    webbrowser.open('https://moodle.astanait.edu.kz/mod/assign/view.php?id=89427')

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id,f'Привет,{ message.from_user.first_name} { message.from_user.last_name}')

@bot.message_handler()
def info(message):
    if message.text.lower():
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message,f'ID: { message.from_user.id }')


bot.polling(non_stop=True)