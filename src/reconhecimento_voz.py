import pyaudio
from vosk import Model, KaldiRecognizer
import json

def ouvir_comando():
    try:
        # Inicializa o modelo
        model_path = "models/vosk_model"  # Caminho para o modelo Vosk
        model = Model(model_path)
        recognizer = KaldiRecognizer(model, 16000)

        # Configura o microfone
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

    except Exception as e:
        print(f"Erro no reconhecimento de voz: {e}")
        return ""
