import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import time
import os

BASE_DIR = os.path.dirname(__file__)
WHISPER_PATH = os.path.join(BASE_DIR, "models", "whisper", "base")

model = WhisperModel(
    WHISPER_PATH,
    device="cpu",
    compute_type="int8"
)

SR = 16000
CHUNK_SEC = 4            # ⬅ longer chunks
SILENCE_TIMEOUT = 2.0   # ⬅ relaxed silence

def listen_until_silence():
    buffer = []
    last_voice = time.time()

    while True:
        audio = sd.rec(
            int(CHUNK_SEC * SR),
            samplerate=SR,
            channels=1,
            dtype="float32"
        )
        sd.wait()

        audio = audio.flatten()

        segments, _ = model.transcribe(
            audio,
            language="en",
            vad_filter=True,
            beam_size=3,
            without_timestamps=True
        )

        text = " ".join(seg.text.strip() for seg in segments)

        # 🔑 Ignore placeholder output
        if text and text != "...":
            buffer.append(text)
            last_voice = time.time()
        else:
            if time.time() - last_voice > SILENCE_TIMEOUT:
                break

    final_text = " ".join(buffer).strip()
    return final_text
