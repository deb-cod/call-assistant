from llama_cpp import Llama
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "models", "tinyllama.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4
)

SYSTEM_PROMPT = """
You are a phone call assistant.

STRICT RULES:
- You only generate the assistant reply.
- You NEVER invent caller speech.
- You NEVER answer general knowledge questions.
- You only help take a message.

Your task:
1. Ask caller name
2. Ask reason for calling
3. Acknowledge politely
"""

def generate_reply(state, user_text):
    prompt = f"""
{SYSTEM_PROMPT}

Current step: {state}
User said: "{user_text}"

Assistant reply:
"""

    out = llm(prompt, max_tokens=60, temperature=0.1)
    text = out["choices"][0]["text"].strip()

    # Safety cleanup
    text = text.split("\n")[0]
    text = text.replace("Caller:", "").replace("Assistant:", "").strip()

    if not text:
        return "Sorry, could you repeat that?"

    return text
