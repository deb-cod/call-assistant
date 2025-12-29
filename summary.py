from llm import llm

def summarize_call(transcript):
    prompt = f"""
Summarize the following phone call in 2–3 sentences.
Focus only on the caller's intent.

Transcript:
{transcript}

Summary:
"""
    out = llm(prompt, max_tokens=80, temperature=0.3)
    text = out["choices"][0]["text"].strip()

    # safety cleanup
    return text.split("\n")[0]
