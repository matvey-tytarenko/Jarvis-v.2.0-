import vosk
import sys
import sounddevice as sd
import queue
import json

model = vosk.Model("model-small")
sample_rate = 16000
device = 1
channel = 1
dtype = 'int16'
block_size = 8000

q = queue.Queue()

def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen(callback):
    with sd.RawInputStream(samplerate=sample_rate, blocksize=block_size, device=device, 
                           dtype=dtype,
                           channels=channel, callback=q_callback):
        rec = vosk.KaldiRecognizer(model, sample_rate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])