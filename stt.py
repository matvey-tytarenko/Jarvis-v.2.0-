import torch
import sounddevice as sd
import time
from datetime import datetime
from num2words import num2words
import playsound as ps
import random

now = datetime.now()

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'aidar'
put_accent = True
put_yoo = True
device = torch.device('cpu')
text = "Здравcтвуйте джарвис на связи"

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)
model.to(device)

def Jarvis(text: str):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)
    print(text)

    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate * 2)
    sd.stop()