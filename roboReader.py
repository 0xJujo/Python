import pyttsx3

print ("Hello people my name is Robo and I am here to assist you in vocalising your thoughts")
while(True):
    x= input ("What do you want me to say? ")
    if (x=="q"):
        break
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()