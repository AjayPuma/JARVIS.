import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    # speak("I'm mr. naags, please tell me how I can help you.")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "none"
    return query

def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ajaypuma2004@gmail.com' , 'santhimadhav2004')
    server.sendmail('ajaypuma2004@gmail.com' , to , content)
    server.close()

if __name__ == "__main__":
    speak("Hello")
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open chat google' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)    

        # elif 'open whatsapp' in query:
        #     codePath = "C:\\Users\\ajayp\\AppData\\Local\\Programs\\Microsoft VS Code\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)   
            
        elif 'open chat g.p.t' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe"  
            os.startfile(codePath)      
            
        elif 'open brave' in query:
            codePath = "C:\\Users\\ajayp\\Desktop\\Brave.lnk"
            os.startfile(codePath)     
            
        elif 'open canvas' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe" 
            os.startfile(codePath)     
    
        elif 'play music' in query:
            music_dir = "C:\\Users\\ajayp\\Downloads\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")  
            
        elif 'open vscode' in query:
            codePath = "C:\\Users\\ajayp\\AppData\\Local\\Programs\\Microsoft VS Code\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    
            
        elif 'email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "ajaypuma2004@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:  
                print(e)
                speak("sorry can't sent email")
