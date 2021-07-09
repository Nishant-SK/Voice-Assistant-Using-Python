
#first read readme.me file to know about what queries this chatbot currently can respond too.

import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser


engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 120)

engine.say("hello jarvis here, what's your name master ")
engine.runAndWait()

r = sr.Recognizer()
mic = sr.Microphone()


#1st query(tell your name only)
with mic as source:
    print("speak now")
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    audio = r.listen(source)


print("recognizing")
try:
    output1 = r.recognize_google(audio)
    print("hello " + output1 + " how are u doing?")
    engine.say("hello " + output1 + " how are u doing ?")
    engine.runAndWait()
except:
    print("cannot hear you clearly but nice to meet you sir , how are u doing? ")
    engine.say("cannot hear you clearly but nice to meet you sir , how are u doing? ")
    engine.runAndWait()

#2nd query(u can say "doing well","nice" or leave it unanswered)
with mic as source:
    print("speak now")
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    audio = r.listen(source)

print("recognizing")
try:
        output2 = r.recognize_google(audio)
        if output2 == "doing well":
            print("and the weather too , pretty well")
            engine.say("and the weather too , pretty well")
            engine.runAndWait()
        elif output2 == "nice":
            print("just likes today weather , its sunny and nice")
            engine.say("just likes today weather , its sunny and nice")
            engine.runAndWait()
        else:
            print("i hope u are doing great")
            engine.say("i hope u are doing great")
            engine.runAndWait()
except:
    print("speak clearly sir ")
    engine.say("speak clearly sir ")
    engine.runAndWait()

time = str(datetime.datetime.now())
hour = int(time[11:13])
min = int(time[14:16])

#3rd query(u can say "tell me the current time" or leave it unanswered)
with mic as source:
    print("speak now")
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    audio = r.listen(source)

print("recognizing")
try:
        output3 = r.recognize_google(audio)
        if output3 == "tell me the current time":
            print("sir it is " + str(hour) + " hours and " + str(min) + " minutes")
            engine.say("sir it is " + str(hour)+" hours and " + str(min) + " minutes")
            engine.runAndWait()
        else:
            if 0 < hour < 12:
                print("by the way good morning sir")
                engine.say("by the way good morning sir")
                engine.runAndWait()
            elif 12 < hour < 16:
                print("by the way good afternoon sir")
                engine.say("by the way good afternoon sir")
                engine.runAndWait()
            elif 16 < hour < 21:
                print("by the way good evening sir")
                engine.say("by the way good evening sir")
                engine.runAndWait()
            else:
                print("by the way ,its too late sir , you must get some rest")
                engine.say("by the way ,its too late sir , you must get some rest")
                engine.runAndWait()

except:
    print("cannot hear you sir")
    engine.say("cannot hear you sir")
    engine.runAndWait()

#4th query(u can say "open google", " open wikipedia" or leave it unanswered)
with mic as source:
    print("speak now")
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    audio = r.listen(source)

print("recognizing")
try:
        output3 = r.recognize_google(audio)
        if output3 == "open Google":
            print("opening google")
            engine.say("opening google")
            engine.runAndWait()
            webbrowser.open("www.google.com")
        elif output3 == "open Wikipedia":
            print("opening wikipedia")
            engine.say("opening wikipedia")
            engine.runAndWait()
            webbrowser.open("https://www.wikipedia.org")
        else:
            print("bye")
            engine.say("bye")
            engine.runAndWait()

except:
    print("cannot hear you sir")
    engine.say("cannot hear you sir")
    engine.runAndWait()