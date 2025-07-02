import speech_recognition as sr
import pyttsx3
import streamlit as st
import json

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')

for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
        
# Store appointments in dictionary
appointments = {}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

def book_appointment():
    speak("Please tell you name.")
    name = listen()
    if not name:
        return

    speak("Please say the date of appointment.")
    date = listen()
    if not date:
        return

    speak("Please say the time of appointment.")
    time = listen()
    if not time:
        return

    speak("Please tell the favourable place.")
    time = listen()
    if not place:
        return

    # Store appointment
    key = f"{date} {time}"
    if key in appointments:
        speak("Sorry, this slot is already booked.")
    else:
        appointments[key] = name
        speak(f"Appointment booked for {name} on {date} at {time} and {place}.")

def main():
    st.title("Ai Voice Agent")
    st.image("Ai Voice Agent.jpg", width=1200)
    st.button("Schedule Appointment")
    speak("Welcome to your Tail Chatai booking assistant.")
    while True:
        speak("Say 'book' to schedule an Pleasure appointment or 'exit' to stop.")
        command = listen()

        if "book" in command:
            book_appointment()
            speak("Your appointment has been scheduled with Dinesh Rangbas have good time with him. Thank you. Goodbye!")
            break  
        elif "exit" in command:
            speak("Goodbye.")
            break
        else:
            speak("Please say a valid command.")

if __name__ == "__main__":
    main()