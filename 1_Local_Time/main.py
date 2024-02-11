import time
import pyttsx3


engine= pyttsx3.init()
chatStr = ""

def say(text):
    engine.say(text)
    engine.runAndWait()


t = time.localtime(time.time())
local_time =time.asctime(t)

print("local time : " + time.asctime(t))
say("local time : " + time.asctime(t))
