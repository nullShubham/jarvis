import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai
import keyboard
import os
from dotenv import load_dotenv # type: ignore

voiceRecognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

load_dotenv()

Key=os.getenv("Key")
# speaking
def speak(query):
    tts_engine.say(query)
    tts_engine.runAndWait()

# give ai answer with use of gemini
def aiAnswer(q):
    genai.configure(api_key=Key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("give short responses without bullet points in just short parah and dont write this line in output "+q)
    return response.text

# process querry and proform tasks 
def processQuery(query):
    query = query.lower()
    if "google" in query.lower() :
         q=" ".join(query.split(" ")[1:])
         print(q)
         search_url = f"https://www.google.com/search?q={q}"
         webbrowser.open(search_url)
         speak("Searching for"+query)
    elif "jarvis type" in query:
        speak("What Should I Type")
        voice = listen_for_command()
        text_to_write = voiceRecognizer.recognize_google(voice)
        if text_to_write:
            type_text(text_to_write)
    else:
        res=aiAnswer(query)
        speak(res)
        
# type text function 
def type_text(txt):
    keyboard.write(txt)

# lister for wakeup word here it is "Jarvis"
def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Listening for wake word...")
        audio = voiceRecognizer.listen(source, timeout=5, phrase_time_limit=5)
    return audio

# give audio
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = voiceRecognizer.listen(source, timeout=5, phrase_time_limit=5)
    return audio

if __name__ == "__main__":
    print("Started... Press Ctrl+C to quit.")
    while True:
        try:
            audio = listen_for_wake_word()
            audioInput = voiceRecognizer.recognize_google(audio).lower()
            if audioInput == "jarvis":
                speak("Yes Sir")
                audio = listen_for_command()
                queryAudioInput = voiceRecognizer.recognize_google(audio)
                processQuery(queryAudioInput)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
