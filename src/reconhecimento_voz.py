import pyaudio
from vosk import Model, KaldiRecognizer
import json

def ouvir_comando():
    model = Model("models/vosk_model")
    recognizer = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Diga algo...")
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            resultado = json.loads(recognizer.Result())
            comando = resultado.get("text", "")
            print("Você disse:", comando)
            return comando