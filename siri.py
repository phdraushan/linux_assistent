import openai
import speech_recognition as sr
import pyttsx3
import os
import time
import subprocess

openai.api_key = ''

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()


def chat_with_mistral(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message["content"].strip()

def chat_with_tinyllama(prompt):
    result = subprocess.run(
        ["ollama", "run", "tinyllama"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()




def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Listening for the wake word...")
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)
            try:
                # Recognize the speech using Pocketsphinx (can be used offline)
                recognized_text = recognizer.recognize_google(audio)
                print(f"Recognized: {recognized_text}")

                # Trigger the assistant if the wake word is detected
                if "hey" in recognized_text.lower():
                    print("Wake word detected, activating assistant...")
                    speak("Hello, how can I assist you?")
                    return True
            except sr.UnknownValueError:
                pass  # Ignore if nothing recognized
            except sr.RequestError:
                print("Error with speech recognition service.")
                break


def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech service.")
        return None


def run_assistant():
    while True:
        # Wait for the wake word
        # if listen_for_wake_word():
            # After detecting "Hey Buddy", listen for the actual command
            command = listen_for_command()
            if command:
                # Send the command to GPT for processing
                response = chat_with_tinyllama(command)
                speak(response)

# Start the assistant
if __name__ == "__main__":
    run_assistant()



