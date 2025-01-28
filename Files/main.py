import speech_recognition as sr
import pyttsx3
import datetime
import wikipediaapi
import webbrowser
import os
import wikipedia
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import wikipediaapi
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

print("Loading your AI personal assistant - Velion")

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greeting function based on time of day
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif 12 <= hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")



# Function to recognize user voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Calibrate for ambient noise
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")
        except sr.UnknownValueError:
            speak("I'm sorry, I didn't catch that. Could you please repeat?")
            return "None"
        except sr.RequestError:
            speak("Sorry, I can't connect to the speech recognition service.")
            return "None"
        return statement.lower()

# Wikipedia search function


# Spotify credentials
SPOTIPY_CLIENT_ID = "a013d93c5f754101a75ac93af8d84065"
SPOTIPY_CLIENT_SECRET = "e0738d7da50c4043999cf9a8a91d64bf"

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

# Spotify play music function
def play_music_on_spotify(query):
    try:
        results = sp.search(q=query, type='track', limit=1)
        tracks = results['tracks']['items']

        if tracks:
            track = tracks[0]
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            spotify_url = track['external_urls']['spotify']

            speak(f"Playing {track_name} by {artist_name}.")
            print(f"Playing {track_name} by {artist_name}. Link: {spotify_url}")
            webbrowser.open(spotify_url)
        else:
            speak("Sorry, I couldn't find any matching songs on Spotify.")
    except Exception as e:
        speak("There was an issue accessing Spotify.")
        print(e)

# Main program starts here
wishMe()


if __name__ == '__main__':
    while True:
        speak("How can I assist you?")
        statement = takeCommand()

        # Continue if no command was detected
        if statement == "none":
            continue

        # Exit condition
        if "good bye" in statement or "ok bye" in statement or "stop" in statement or 'goodbye' in statement:
            speak("Your personal assistant Velion is shutting down. Goodbye!")
            print("Your personal assistant Velion is shutting down. Goodbye!")
            break

        elif statement.startswith("play "):
            song_query = statement.replace("play ", "").strip()
            play_music_on_spotify(song_query)


        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)


        elif 'how are you' in statement or 'how r u' in statement:
            speak("I am doing well, thank you for asking!")

        elif 'purpose' in statement:
            speak("I am an AI assistant designed to assist you with various tasks and answer your questions")
        elif 'developer' in statement:
            speak("I was developed by Arnav Srivastava of class 8 b of Delhi Public School Dibrugarh")

        # Weather functionality using WeatherAPI
        elif "weather" in statement:
            api_key = "caddc69f50ea4a08bd5152014241004"  
            base_url = "http://api.weatherapi.com/v1/current.json?"
            speak("Please tell me the name of a place.")
            city_name = takeCommand()
            if city_name != "none":
                complete_url = base_url + "key=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if "error" not in x:
                    current_temperature = x['current']['temp_c']
                    current_humidity = x['current']['humidity']
                    weather_description = x['current']['condition']['text']
                    speak(f"The temperature in {city_name} is {current_temperature} degrees Celsius with {weather_description} and humidity at {current_humidity} percent.")
                    print(f"Temperature (Celsius): {current_temperature}\nHumidity: {current_humidity}\nDescription: {weather_description}")
                else:
                    speak("City not found.")
            else:
                speak("I couldn't get the city name. Please try again.")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement or 'hu r u' in statement:
            speak("I am Velion, version 1.0, your personal assistant. I can open YouTube, Google Chrome, Gmail, Stack Overflow, tell you the time, search Wikipedia, get weather updates, and fetch news.")

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Arnav Srivastava.")
            print("I was built by Arnav Srivastava.")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is Stack Overflow")

        elif "design" in statement or "structure" in statement:
            speak("I am a simple text-based AI assistant. My structure is based on a combination of multiple APIs and code")

        elif "languages" in statement:
            speak("I am currently limited to speak and understand English.")

        elif "umang" in statement:
            speak("Umang is a place to showcase your talent in front of the world. This mega exhibition is hosted at Delhi Public School Dibrugarh.")

        elif "delhi public school dibrugarh" in statement or "dps dibrugarh" in statement:
            speak("DPS Dibrugarh is a renowned school emphasizing academic excellence and character development. It offers a supportive environment and encourages extracurricular activities and community service.")

        elif "programming language" in statement:
            speak("Python is one of the primary programming languages used in my development.")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times of India, happy reading")
            time.sleep(6)

        elif 'search' in statement:
            statement = statement.replace("search", "").strip()
            search_url = f"https://www.google.com/search?q={statement.replace(' ', '+')}"
            webbrowser.open_new_tab(search_url)
            speak(f"Here are the search results for {statement}")
            time.sleep(5)

        

        
        


        elif 'ask' in statement:
            speak("I can answer computational and geographical questions. What would you like to ask?")
            question = takeCommand()
            app_id = "T4W36L-RU4T65UHAU"  # Wolfram Alpha API key
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            try:
                answer = next(res.results).text
                speak(answer)
                print(answer)
            except StopIteration:
                speak("Sorry, I couldn't find an answer to that question.")

        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your PC will log off in 10 seconds. Please exit all applications.")
            subprocess.call(["shutdown", "/l"])

        

    time.sleep(3)