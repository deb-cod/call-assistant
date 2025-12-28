# tts.py
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print("🔊 Speaking:", text)
    speaker.Speak(text)

