# llm.py
def generate_reply(user_text):
    if not user_text:
        return "Hello, may I know who is calling?"

    return f"Okay, I got your message: {user_text}. I will inform the user."
