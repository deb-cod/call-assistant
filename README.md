# call-assistant

## High level architecture: 

        Incoming Call
                ↓
        CallScreeningService (Android)
                ↓ (15 sec timer)
        If user doesn't answer
                ↓
        Auto-answer call
                ↓
        Audio Stream (Mic + Speaker)
                ↓
        Speech-to-Text (Local)
                ↓
        Local LLM (Response generation)
                ↓
        Text-to-Speech (Local)
                ↓
        Caller hears AI voice


## File Structure:

                call-assistant/
                │
                ├── assistant_core.py        # Entry point (Android will call this)
                ├── conversation.py          # Call flow + state machine
                ├── llm.py                   # Local LLM (TinyLlama / Phi)
                ├── stt_whisper_stream.py    # Streaming Whisper STT (optimized)
                ├── memory.py                # Call transcript storage
                │
                ├── models/
                │   ├── tinyllama.gguf       # LLM model, this needs to be downloaded locally | because this is llm model which is really has large fiel size, so stop complaning and read this 😐 
                │   └── whisper/             # Whisper models | download this using `git clone https://huggingface.co/Systran/faster-whisper-base`
                │
                └── requirements.txt
