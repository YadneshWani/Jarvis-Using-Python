import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyowm

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour =int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning Sir!")
        
    elif(hour>=12 and hour<18):
        speak("Good Afternoon Sir!")
        
    elif(hour>=18 and hour<20):
        speak("Good Evening Sir!")
    else:
        speak("Good Night!")
        
    speak("Hi i am Jarvis sir. How may i help you ?")

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=1500
        audio=r.listen(source)


    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yadneshwani0987@gmail.com','yadnesh@123')
    server.sendmail('yadneshwani0987@gmail.com',to,content)
    server.close()


if __name__ =="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open('google.com')
            speak("opening google")

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            speak('opening stackoverflow')

        elif 'play music' in query:
            music_dir='E:\\movies\\NEW AUDIO SONGS'
            songs=os.listdir(music_dir)
            n=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[n]))      #random use kraycha nantr
            speak(f"playing song {songs[n]}")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif 'the date' in query:
            strDate=datetime.datetime.now().strftime("%B:%d:%Y")
            print(strDate)
            speak(f"Sir the Date is{strDate}")

        elif 'open visual code' in query:
                codePath="C:\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                speak("opening Visual Code")

        elif 'open text pad' in query:
                codePath="C:\\Program Files\\TextPad 7\\TextPad.exe"
                os.startfile(codePath)
                speak("opening Textpad")

        elif 'open chrome' in query:
                codePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)
                speak("opening google chrome")

        elif 'send email' in query:
            try:
                speak('What do you want to send')
                content=takeCommand()
                to='yadneshwani123@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak("Sorry Sir! not able to send Email")

        elif 'hi jarvis' in query:
            speak("hi Yadnesh!")

        elif 'thank you jarvis' in query:
            speak("Welcome Yadnesh!")


        elif 'play video song' in query:
            video_dir='E:\\movies\\VIDEO SONGS'
            vSongs=os.listdir(video_dir)
            no=random.randint(0,len(vSongs))
            os.startfile(os.path.join(video_dir,vSongs[no]))
            speak(f"playing song {vSongs[no]}")


        elif 'the weather' in query:
            try:
                owm = pyowm.OWM('2c4be2938e71b053e30079edfb5232a6')

                #ow_url = "http://home.openweathermap.org/api_keys"
                speak("Enter city name: ")
                city=takeCommand()
                loc=owm.weather_at_place(city)
                weather=loc.get_weather()

                temp=weather.get_temperature(unit='celsius')
                temperature=temp.items()
                speak(temperature)


            except Exception as e:
                print(e)
                speak("Problem occur while checking wheather")

                

                

            
    
