import time
import threading
from kivy.app import App
from kivy.uix.label import Label
from jnius import autoclass
from llama_cpp import Llama
from vosk import Model, KaldiRecognizer
import pyttsx3

# Android System Classes
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
TelephonyManager = autoclass('android.telephony.TelephonyManager')
AudioManager = autoclass('android.media.AudioManager')


class AICallBot(App):
    def build(self):
        self.label = Label(text="Bot Active: Waiting for Call")
        # Load Local AI
        self.llm = Llama(model_path="models/qwen.gguf", n_ctx=512)
        self.stt_model = Model("models/vosk-model")
        self.engine = pyttsx3.init()

        # Start Call Monitoring Thread
        threading.Thread(target=self.monitor_calls, daemon=True).start()
        return self.label

    def monitor_calls(self):
        tm = PythonActivity.mActivity.getSystemService(Context.TELEPHONY_SERVICE)
        while True:
            state = tm.getCallState()
            if state == TelephonyManager.CALL_STATE_RINGING:
                print("Detected Ringing... Waiting 20s")
                time.sleep(20)
                # Check if still ringing
                if tm.getCallState() == TelephonyManager.CALL_STATE_RINGING:
                    self.start_ai_session()
            time.sleep(1)

    def start_ai_session(self):
        # Force Speakerphone so the AI can 'hear' the caller
        audio = PythonActivity.mActivity.getSystemService(Context.AUDIO_SERVICE)
        audio.setMode(AudioManager.MODE_IN_CALL)
        audio.setSpeakerphoneOn(True)

        # Voice Loop
        self.engine.say("Hello, I am a local AI assistant answering for my owner. How can I help?")
        self.engine.runAndWait()
        # Add your STT -> LLM -> TTS loop logic here
