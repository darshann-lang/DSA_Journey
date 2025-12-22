# Install an external module and use it to perform an operation of your interest 

'''
For this problem I've used pyttsx3, which basically converts the text message into voice.  
'''

import pyttsx3
engine = pyttsx3.init()
engine.say("Hi, I am Darshan, and I'm interested in learning python.")
engine.runAndWait()