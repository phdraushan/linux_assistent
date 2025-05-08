### 📝 **Siri-like Voice Assistant in Terminal (Lubuntu)**

#### ✅ Components Used:

- `speech_recognition` for voice input
    
- `pyttsx3` for voice output (text-to-speech)
    
- `openai` (or `ollama` + local LLM like TinyLLaMA)
    
- Optional wake word: **“Hey Buddy”**
    

#### 🔧 Key Features:

- Voice-activated assistant listens for “Hey Buddy”
    
- Transcribes commands and sends to GPT/local model
    
- Reads out the response
    

#### 🧪 Sample Workflow:

```python
# Setup recognizer, TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Wait for wake word using recognizer.listen()
# On trigger, listen for command and forward to GPT/local model
# Use pyttsx3 to speak out the response
```

#### 🔁 Optional: Replace OpenAI with Local LLM

- Use `ollama` to run a local model like `tinyllama`
    
- Replace OpenAI API calls with subprocess or HTTP calls to `ollama`
# linux_assistent
