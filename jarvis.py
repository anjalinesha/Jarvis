import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import smtplib
import pywhatkit
import sys
import pyjokes
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)  (v[0]-davis,v[1]-zira)
engine.setProperty('voice',voices[1].id)

#text for speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am ziara. Please tell me how can I help you!")


def takecommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('riyaguptamiss123@gmail.com','RiyaPassword@123')
    server.sendmail('riyaguptamiss123@gmail.com',to,content)
    server.close()

#FOR NEWS UPDATE:
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcruch&apiKey=70576b202de547698025e328b136b048'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #print(f"today's {day[i]} news is: ",head[1])
        speak(f"today's {day[i]} news is: {head[i]}")


if __name__ == "__main__":
    wishme()
    while True:

    #if 1:

        query = takecommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=1)
            speak('Acorrding to wikipedia')
            print(results)
            speak(results)

        elif 'songs on youtube' in query :
            speak("which song do you like to hear ")
            song=takecommand().lower()
            pywhatkit.playonyt(f"{song}")

        elif 'open google' in query:
            speak('what should i search on google')
            cm=takecommand().lower()
            webbrowser.open(f'{cm}')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open notepad' in query:
            npath="C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "message" in query:
            pywhatkit.sendwhatmsg("+919182778762","haii this is a protocol! so, plz do not reply", 23,49)

        elif "mail" in query:
            speak("sir what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = ''
                password = ''
                send_to_email = 'mahalakshmir104@gmail.com'



        elif 'open command prompt' in query:
            os.system("start cmd")


        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
               ret, img = cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(50)
               if k==27:
                break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'play songs' in query:
            n = random.randint(0,9)
            print(n)
            music_dir = "D:\\engfav songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")


        elif "thanks" in query:
            speak("thanks for using me mam,have a good day")
            sys.exit()

    #to close any application
        elif "close notepad" in query:
            speak("okay! closing notepad")
            os.system("taskkill /f /im notepad.exe")

    #to set alarm:
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour())
            if nn==22:
                music_dir=''
                songs = os.listdir(music_dir)
                os.startfile(os.path(music_dir, songs[0]))
    #find a joke
        elif "joke" in query:
            joke = pyjokes.get_joke('en')
            speak(joke)

        elif "shut down" in query:
            os.system('shutdown /s /t 5')

        elif "restart" in query:
            os.system('shutdown /r /t 5')

        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll.SetSuspendState 0,1,0")

    #switch the window
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "news" in query:
            speak("please wait sir,feteching the latest news")
            news()


        speak("do you have any other work ")