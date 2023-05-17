# Jarvis 2.0
import config, stt, tts
import playsound as ps
from fuzzywuzzy import fuzz
from datetime import datetime
import openai
import pyautogui as pg
import webbrowser
import random
from num2words import num2words
import os
import subprocess
import time
import telebot

from sound import Sound

sounds = ['Audio\\Загружаю сэр.wav', 'Audio\\Запрос выполнен сэр.wav']
bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

print(f"{config.NAME} (v{config.VER}) начал свою работу...")
ps.playsound('Audio\\Jarvis.wav')
print('Github: https://github.com/matvey-tytarenko/Jarvis-v.2.0-')

def response(voice: str):
    print(voice)
    if voice.startswith(config.ALIAS):

        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.CMD_LIST.keys():
            ps.playsound('Audio\\Wrong.wav')
        else:
            execute_cmd(cmd['cmd'])

def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.ALIAS:
        cmd = cmd.replace(x, '').strip()

    for x in config.TBR:
        cmd = cmd.replace(x, '').strip()

    return cmd

def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc

def date():
   now = datetime.now()

   if now.day and now.month < 10:
      num2words(0, lang='ru') + num2words(now.day, lang='ru') + '.' + num2words(0, lang='ru') + num2words(now.month, lang='ru')
   else:
       num2words(now.day, lang='ru') + num2words(now.month, lang='ru')

def execute_cmd(cmd: str):

    jarvis = ps.playsound(random.choice(sounds))

    now = datetime.now()

    if cmd == 'help':
        text = 'Я умею: ...'
        text += '\nпроизносить дату и время ...'
        text += '\nоткрывать приложения'
        stt.Jarvis(text)

    elif cmd == 'ctime':
        stt.Jarvis('Сейчас: ' + num2words(now.hour, lang='ru') + ' : ' + num2words(now.minute, lang='ru'))
    elif cmd == 'day':
        now = datetime.now()
        stt.Jarvis('Сегодня: ' + num2words(now.day, lang='ru') + '.' + num2words(now.month, lang='ru') + '.' + num2words(now.year, lang='ru'))
    elif cmd == 'youtube':
        jarvis
        pg.hotkey('winLeft')
        pg.write('youtube')
        pg.hotkey('Enter')
    elif cmd == 'viber':
        jarvis
        pg.hotkey('winLeft')
        pg.write('Viber')
        pg.hotkey('Enter')
    elif cmd == 'telegram':
        jarvis
        pg.hotkey('winLeft')
        pg.write('Telegram')
        pg.hotkey('Enter')

    elif cmd == 'code':
        jarvis
        os.system('code')
        ps.playsound('Audio\\Мы работаем над проектом сэр.wav')
    elif cmd == 'thanks':
        ps.playsound('Audio\\услугам сэр.wav')
    elif cmd == 'music':
        jarvis
        pg.hotkey('winLeft')
        pg.write('youtube Music', 0)
        pg.hotkey('Enter')
        time.sleep(0.5)
        pg.click(1940, 425)
    elif cmd == 'restart':
        jarvis
        os.system('shutdown /r /t 0')
    elif cmd == 'poweroff':
        ps.playsound('Audio\\System_diagnostic.wav')
        os.system('shutdown /s /t 0')
    elif cmd == 'anime':
        jarvis
        pg.hotkey('winLeft')
        pg.write('AniLibrix', 0)
        pg.hotkey('Enter')
    elif cmd == 'github':
        jarvis
        webbrowser.open('https://github.com/matvey-tytarenko')
    elif cmd == 'pause_and_continue':
        jarvis
        pg.hotkey('space')
    elif cmd == 'fullscreen':
        jarvis
        pg.hotkey('f')
    elif cmd == 'language':
        jarvis
        pg.hotkey('shift', 'alt')
    elif cmd == 'screenshot':
        jarvis
        screenshot = pg.screenshot()
        screenshot.save('screenshot.png')
        os.system('screenshot.png')
    elif cmd == 'volumeup':
        jarvis
        Sound.volume_set(60)
    elif cmd == 'volumedown':
        jarvis
        Sound.volume_set(20)
        

tts.listen(response)