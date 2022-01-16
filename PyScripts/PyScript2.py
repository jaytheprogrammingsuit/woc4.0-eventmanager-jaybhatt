'''
PyScript 2 - 'Text to speech'
Author: Jay Bhatt

Desc: This Python script is used to convert text to speech and save .mp3 file.
    # In this python script i used 2 libraries gtts and playsound.
'''
from gtts import gTTS
from playsound import playsound

def speechText(msg) :
    speech = gTTS(text = msg)
    speech.save('dataAudio.mp3') #create mp3 file and save
    playsound("D:\WOC4-Django\woc4.0-eventmanager-jaybhatt\PyScripts\dataAudio.mp3")   #play mp3 file

#read the file 'data.txt'
readFile = open("data.txt", "r")

#read the data from file and store it into 'msg' variable
msg = readFile.read()
speechText(msg)
print(msg)

#close the file
readFile.close()