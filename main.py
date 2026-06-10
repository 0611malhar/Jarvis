import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import musicLib
import requests

recognizer = sr.Recognizer()
newsapi = "d2855d7b90604947b1b1c894c3c17a85"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

news_index = 0

def process_command(c):


    if "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open twitter" in c.lower():
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")

    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open github" in c.lower():
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif "open whatsapp" in c.lower():
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[-1]
        link = musicLib.music[song]
        webbrowser.open(link)

    
    elif "news" in c.lower():
        global news_index

        r = requests.get(
            f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey=d2855d7b90604947b1b1c894c3c17a85"
        )

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            #next 5 headlines
            next_articles = articles[news_index:news_index + 5]

            if next_articles:
                for article in next_articles:
                    speak(article["title"])

                news_index += 5
            else:
                speak("No more news available.")

    elif "exit" == c.lower():
        speak("Exiting Jarvis. Have a great day!")
        exit()


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)

            wd = r.recognize_google(audio)

            if wd.lower() == 'jarvis':
                print("Jarvis activated...")
                speak("Yes, need help?")
                time.sleep(2)
                break

        except Exception as e:
            print(f"Error: {e}")

    while True:
        r = sr.Recognizer()

        try:    # listen for cmd

            with sr.Microphone() as source:
                audio = r.listen(source)

            command = r.recognize_google(audio)
            process_command(command)

        except Exception as e:
            print(f"Error: {e}")