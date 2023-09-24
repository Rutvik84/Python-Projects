import speech_recognition as sr
import pyttsx3
import datetime
import calendar
import wikipedia
import webbrowser
import subprocess
import pause
import wolframalpha
import requests
import json


MASTER = "sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning "+ MASTER)
    elif hour>=12 and hour <18:
        print("Good Afternoon "+ MASTER)
        speak("Good Afternoon " + MASTER)
    else:
        print("Good Evening " + MASTER)
        speak("Good Evening "+ MASTER)

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        audio  = r.listen(source)

        query = " "

    try :
        print("recognizing...")
        query = r.recognize_google(audio,language='en-us')
        print("You said: " + query)


    except Exception as e:
        speak("Say That again !")
        query = "None"
    return query

print("Initializing ...")
speak("Initializing ...")
print(f"Hello{MASTER}")
speak(f"Hello{MASTER}")
wishme()
speak(f"{MASTER} What do you want me to do for you : ")

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def assistant(query):



    if 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current Time is {time}")
        print(f"{time}")

    elif "wikipedia" in query :
        query = query.replace('wikipedia','')
        speak("Searching Wikipedia ...")
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

        print("Done Sir, Anything Else !")
        speak("Done Sir, Anything Else !")

    elif "who are you" in query :
        print("I am your Assistant Pheonix. i can look up answers for you and if you need anything just ask. Your wish is my command")
        speak("I am your Assistant Pheonix. i can look up answers for you and if you need anything just ask. Your wish is my command")

    elif "why do you exist" in query or "why did you come" in query:
        speak(f"It is a secret.")

    elif "how are you" in query:
        print("I am fine, Thank you for asking!. This is challenging time for us. i hope your and your loved ones are safe and healthy")
        speak("I am fine, Thank you for asking!. This is challenging time for us. i hope your and your loved ones are safe and healthy")
        print("\nHow are you?")
        speak("\nHow are you?")

    elif "so lets move on" in query :
        speak("what you want me to do sir")

    elif "fine" in query or "good" in query:
        print("It's good to know that you are fine")
        speak("It's good to know that you are fine")

    elif "spotify" in query :
        print("Opening Spotify")
        speak("Opening Spotify")
        subprocess.Popen(["C:\\Users\\rutvi\\AppData\\Roaming\\Spotify\\Spotify.exe"])

        print("Spotify Opened , Anything Else Sir")
        speak("Spotify Opened , Anything Else Sir")

    elif "steam" in query :
        speak("Let's get some frags Sir")
        result = subprocess.Popen(["D:\STEAM\\steam.exe"], shell=True)

        speak("Done Sir, Anything Else !")

    elif "open" in query :
        try :
            website = query.split(' ')
            webbrowser.open("https://"+website[website.index("open")+1]+".com")
            speak(website[website.index("open")+1] + "is Opened ")
        except Exception as e :
            speak("i can't see it")

    elif "calculate" in query:
        app_id = "XXX"
        client = wolframalpha.Client(app_id)
        ind = query.lower().split().index("calculate")
        text = query.split()[ind + 1:]
        res= client.query(" ".join(text))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)

    elif "what is" in query or "who is" in query:
        app_id = "XXX"
        client = wolframalpha.Client(app_id)
        ind = query.lower().split().index("is")
        text = query.split()[ind + 1:]
        res = client.query(" ".join(text))
        answer = next(res.results).text
        print(answer)
        speak(answer)

    elif "note" in query or "remember this" in query:
        speak("What would you like me to write down?")
        note_text = takecmd()
        note(note_text)
        speak("I have made a note of that.")
        speak("Anything else sir !")

    elif "where is" in query :
        ind = query.lower().split().index("is")
        location = query.split()[ind + 1:]
        url = "https://www.google.com/maps/place/" + "".join(location)
        speak("This is where " + str(location) + " is.")
        webbrowser.open(url)

    elif "search" in query.lower ():
        ind = query.lower().split().index("search")
        search = query.split()[ind + 1:]
        webbrowser.open(
            "https://www.google.com/search?q=" + "+".join(search))
        speak("Searching " + str(search) + " on google")

    elif "weather" in query:
        key = "XXXX"
        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
        ind = query.split().index("in")
        location = query.split()[ind + 1:]
        location = "".join(location)
        url = weather_url + "appid=" + key + "&q=" + location
        js = requests.get(url).json()
        if js["cod"] != "404":
            weather = js["main"]
            temperature = weather["temp"]
            temperature = temperature - 273.15
            humidity = weather["humidity"]
            desc = js["weather"][0]["description"]
            weather_response = " The temperature in Celcius is " + str(temperature) + " The humidity is " + str(
                humidity) + " and The weather description is " + str(desc)
            print(weather_response)
            speak(weather_response)
        else:
            speak("City Not Found")

    elif "play" in query :
            website = query.split('play')
            webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(website) )
            print("playing " + str(website) + " on youtube")
            speak("playing " + str(website) + " on youtube")


    elif "sleep" in query or "stop" in query or "do not listen" in query:
        speak("for how many seconds do you want me to sleep")
        a = int(takecmd())
        pause.sleep(a)
        speak(str(a) + f" seconds completed {MASTER}. Now you can ask me anything")

    elif "goodbye" in query :
        speak(f"My pleasure to help you {MASTER}, See you later")
        return 0


    else:
        speak("It seems its out of my own way lets try it later  !")


while True:
    if assistant(takecmd().lower())==0:
      break
