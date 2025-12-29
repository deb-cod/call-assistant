call_log = []

def add(role, text):
    call_log.append(f"{role}: {text}")

def get_history():
    return "\n".join(call_log)

def reset():
    call_log.clear()
