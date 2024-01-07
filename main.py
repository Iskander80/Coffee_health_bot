import asyncio
import sys
import telebot
import urls
from tests import tests_services
import time
import schedule
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import aioschedule


bot = AsyncTeleBot(urls.BOT_TOKEN, disable_notification=True)

markup1 = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
menu_btn = types.KeyboardButton('В начало')
markup1.row(menu_btn)

@bot.message_handler(func=lambda callback: True)
async def main(message):
    markup = types.InlineKeyboardMarkup()
    btn_available_devices = types.InlineKeyboardButton('Проверить достуность кофемашин', callback_data='PING_DEV')
    markup.row(btn_available_devices)
    await bot.send_message(message.from_user.id,
                           f"Привет, {message.from_user.first_name}! " "Я мониторю кофемашины",
                           reply_markup=markup)

    markup1 = types.ReplyKeyboardMarkup(is_persistent=True, resize_keyboard=True)
    menu_btn = types.KeyboardButton('В начало')
    markup1.row(menu_btn)



@bot.callback_query_handler(func=lambda callback: True)
async def callback_message(callback):
    if callback.data == 'PING_DEV':
        await tests_services.coffee_tests(bot, callback)


@bot.message_handler()
async def start(message):
    if message.text.lower():
        await main(message)


asyncio.run(bot.polling(non_stop=True, request_timeout=90))
asyncio.run(bot.infinity_polling())
