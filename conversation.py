# conversation.py
from stt import listen_and_transcribe
from llm import generate_reply
from tts import speak

def handle_call():
    speak("Hello. This call is answered by an assistant. Please speak.")

    user_text = listen_and_transcribe(6)
    print("Caller said:", user_text)

    reply = generate_reply(user_text)
    print("Assistant:", reply)

    speak(reply)
