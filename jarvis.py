# Jarvis 2.0
import config, stt, tts
import playsound as ps
from fuzzywuzzy import fuzz
from datetime import datetime
import openai
import telebot
import pyautogui as pg
import webbrowser
import random
from num2words import num2words
import os

sounds = ['Audio\\Загружаю сэр.wav', 'Audio\\Запрос выполнен сэр.wav']

print(f"{config.NAME} (v{config.VER}) начал свою работу...")
ps.playsound('Audio\\Jarvis.wav')

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

def execute_cmd(cmd: str):
    if cmd == 'help':
        text = 'Я умею: ...'
        text += '\nпроизносить время ...'
        text += '\nоткрывать приложения'
        stt.Jarvis(text)

    elif cmd == 'ctime':
        now = datetime.now()
        stt.Jarvis('Сейчас: ' + num2words(now.hour, lang='ru') + ' : ' + num2words(now.minute, lang='ru'))
    elif cmd == 'youtube':
        ps.playsound(random.choice(sounds))
        webbrowser.open('youtube.com')
    elif cmd == 'viber':
        ps.playsound(random.choice(sounds))
        pg.hotkey('winLeft')
        pg.write('Viber')
        pg.hotkey('Enter')
    elif cmd == 'telegram':
        ps.playsound(random.choice(sounds))
        pg.hotkey('winLeft')
        pg.write('Telegram')
        pg.hotkey('Enter')

    elif cmd == 'code':
        ps.playsound(random.choice(sounds))
        os.system('code')
        ps.playsound('Audio\\Мы работаем над проектом сэр.wav')


# Start listening commands
print('Говорите...')
tts.listen(response)