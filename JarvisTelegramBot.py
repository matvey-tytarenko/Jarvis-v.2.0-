import telebot
from telebot import types
import config
import pyautogui as pg
import os
import random
import numpy

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здраствуйте, {message.from_user.first_name} {message.from_user.last_name}'
    sticker = '👋'
    markup = types.ReplyKeyboardMarkup()

    bot.send_message(message.chat.id, text=(sticker and mess), reply_markup=markup)

@bot.message_handler(commands=['screenshot'])
def screenshot(message):
    screenshot = pg.screenshot()
    screenshot.save('screenshot.png')
    photo = open('screenshot.png', 'rb')
    bot.send_photo(message.chat.id, photo)

bot.polling(none_stop=True)