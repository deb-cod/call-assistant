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
