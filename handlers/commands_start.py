from aiogram import types
from misc import dp,bot
import sqlite3
from .sqlit import reg_user

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(message.chat.id,'123')

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🍿СКАЧАТЬ ОНЛАЙН🍿', callback_data= f'start_watch_')
    markup.add(bat_a)
    await bot.send_message(message.chat.id, text="""🎬Все новинки фильмов доступны к скачиванию на нашем <b>основном Телеграм канале</b>. 

👨‍💻Приятного просмотра 👇👇👇""",parse_mode='html',reply_markup=markup)

