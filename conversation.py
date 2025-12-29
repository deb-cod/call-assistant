from stt_whisper_stream import listen_until_silence
from name_extractor import extract_name, extract_spelled_name
from memory import reset, add, get_history
from history_store import save_call
from summary import summarize_call

def handle_call():
    reset()

    state = "ASK_NAME"
    caller_name = None
    attempts = 0

    print("Assistant: Hello. May I know who is calling?")

    while True:
        user_text = listen_until_silence()
        if not user_text:
            continue

        print("Caller:", user_text)
        add("Caller", user_text)

        # -------- ASK NAME --------
        if state == "ASK_NAME":
            name = extract_name(user_text)
            attempts += 1

            if name:
                caller_name = name
                reply = f"Did I hear your name as {caller_name}?"
                state = "CONFIRM_NAME"

            elif attempts >= 2:
                reply = "Please spell your name letter by letter."
                state = "SPELL_NAME"

            else:
                reply = "Sorry, I did not catch your name. Please say it again."

        # -------- CONFIRM NAME --------
        elif state == "CONFIRM_NAME":
            t = user_text.lower().strip()

            if t.startswith("yes"):
                reply = f"Thank you {caller_name}. What is this regarding?"
                state = "ASK_REASON"

            elif t.startswith("no"):
                reply = "Please spell your name letter by letter."
                state = "SPELL_NAME"

            else:
                reply = f"Please say YES if your name is {caller_name}, or NO to repeat."

        # -------- SPELL NAME --------
        elif state == "SPELL_NAME":
            spelled = extract_spelled_name(user_text)
            if spelled:
                caller_name = spelled
                reply = f"Thank you {caller_name}. What is this regarding?"
                state = "ASK_REASON"
            else:
                reply = "Please spell your name clearly."

        # -------- ASK REASON --------
        elif state == "ASK_REASON":
            if len(user_text.split()) >= 3:
                reply = "Thank you. I will inform the user."

                add("Assistant", reply)
                transcript = get_history()
                summary = summarize_call(transcript)
                path = save_call(transcript, summary)

                print("📁 Call saved to:", path)
                print("🧾 Summary:", summary)
                break
            else:
                reply = "Could you please briefly explain the reason for your call?"

        print("Assistant:", reply)
        add("Assistant", reply)
