import pyttsx3 as py
import speech_recognition as sr
r=sr.Recognizer()
import webbrowser
sound=py.init()

while(1):
    with sr.Microphone() as source:
        sound.setProperty('rate',145)
        sound.say("what can i help you?")
        sound.runAndWait()
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio=r.listen(source)
    try:
        a=r.recognize_google(audio,language="en")
        c=a.split(' ')
        
        #for name
        if ['my','name','is']==c[:-1]:
            sound.setProperty('rate',145)
            sound.say("Welcome to the Jarvis"+c[-1])
            sound.runAndWait()
        elif ['myself']==c[:-1]:
            sound.setProperty('rate',145)
            sound.say("Welcome to the Jarvis app"+c[-1])
            sound.runAndWait()
        elif ['i','am']==c[:-1]:
            sound.setProperty('rate',145)
            sound.say("Welcome to the Jarvis app"+c[-1])
            sound.runAndWait()
        elif ['this','is']==c[:-1]:
            sound.setProperty('rate',145)
            sound.say("Welcome to the Jarvis app"+c[-1])
            sound.runAndWait()
            
        elif "name" in c:
            sound.setProperty('rate',145)
            sound.say("Welcome to the Jarvis app"+c[-1])
            sound.runAndWait()
            
            
        #for open program
        elif ['open']==c[:-1]:
            sound.setProperty('rate',145)
            sound.say("please wait i open "+c[-1])
            sound.runAndWait()
            webbrowser.open(a[-1])
            
        #open calculator
        elif ['open','calculator']==c:
            sound.setProperty('rate',145)
            sound.say("please wait i open "+c[-1])
            sound.runAndWait()
            webbrowser.open('calc')
        
        #calculator 
        
        elif ["what","is"]==c[:-3]:
            sound.setProperty('rate',145)
            sound.say("please wait i do")
            sound.runAndWait()
        
        elif ["good","morning"]==c:
            sound.setProperty('rate',145)
            sound.say("good morning sir")
            sound.runAndWait()
            
        
        elif 'close' in c:
            sound.setProperty('rate',145)
            sound.say("okay I close the program?thank you for using the jarvis")
            sound.runAndWait()
            break
    except:
        print("sound error")
