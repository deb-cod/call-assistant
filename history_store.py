import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
HISTORY_DIR = os.path.join(BASE_DIR, "call_history")

os.makedirs(HISTORY_DIR, exist_ok=True)

def save_call(transcript, summary):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"call_{timestamp}.txt"
    path = os.path.join(HISTORY_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write("CALL TRANSCRIPT\n")
        f.write("=" * 20 + "\n")
        f.write(transcript + "\n\n")

        f.write("CALL SUMMARY\n")
        f.write("=" * 20 + "\n")
        f.write(summary)

    return path
