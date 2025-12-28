##################################################
#
#     Speech to text using Vosk - offline
#
#################################################

import json
import vosk
import sounddevice as sd

model = vosk.Model("models/vosk-model-small-en-us-0.15/")
recognizer = vosk.KaldiRecognizer(model, 16000)

def listen_and_transcribe(duration=5):
    audio = sd.rec(
        int(duration * 16000),
        samplerate=16000,
        channels=1,
        dtype='int16'
    )
    sd.wait()

    recognizer.AcceptWaveform(audio.tobytes())
    result = json.loads(recognizer.Result())
    return result.get("text", "")