from tkinter import *
from wikipedia import *
import pywhatkit as kit
import pyttsx3

rout = Tk()
rout.geometry('900x900')
rout.title("Darshan's Chatbot")
rout.config(bg='Black')

# backgroung = PhotoImage(geosearch)
# bg = Label(rout,geosearch)
# bg.place(x = 500,y = 600)


label = Label(rout, text='CHAT BOT ', font='times 20 bold', bg='black', fg='white')
label.place(x=0, y=0)

l2 = Label(rout, text='Developer mail-naikdarshan547@gmail.com', font='times 15 bold')
l2.place(x=300, y=15)

command1 = " "
engine = pyttsx3.init()
msg = "Play on youtube"
number = ' '
time = ' '
engine.setProperty('rate', 125)


def send():
    send = 'YOU-->' + e.get()
    txt.insert(END, '\n' + send)

    if "Hii" in e.get():
        txt.insert(END, "\n" + 'BOT--> Hello, How can i help you?')
        engine.say("Hello, How can i help you?")
        engine.runAndWait()
    elif "what kind of stuff" in e.get():
        txt.insert(END, "\n" + 'BOT--> Hahahahaha...')
        engine.say("Iam laughing")
        engine.runAndWait()
    elif "created you" in e.get():
        txt.insert(END, "\n" + 'BOT--> Darshan created me...😀😀')
        engine.say("Darshan Created me, You can see his email above ")
        engine.runAndWait()
    elif "Iam good" in e.get():
        txt.insert(END, "\n" + 'BOT--> ohh ok')
        engine.say("ohh..okk")
        engine.runAndWait()

    elif 'How are you'.lower() in e.get():
        txt.insert(END, "\n" + 'BOT--> Iam fine what about you?')
        engine.say("Iam fine what about you?")
        engine.runAndWait()
    elif 'your name' in e.get():
        engine.say("Still Darshan didnt gave me a name...")
        engine.runAndWait()
        txt.insert(END, "\n" + 'BOT--> Still Darshan didnt gave me a name...😔😔')
    elif 'who are you' in e.get():
        engine.say("Iam an Digital Assistant")
        engine.runAndWait()
        txt.insert(END, "\n" + 'BOT--> Iam an Digital Assistant')
    elif 'whats your job' in e.get():
        engine.say("My job is to help you")
        engine.runAndWait()
        txt.insert(END, "\n" + 'BOT--> My job is to help you')
    elif 'Alexa and Siri' in e.get():
        engine.say("Alexa and Siri are my best friends..")
        engine.runAndWait()
        txt.insert(END, "\n" + 'BOT-->Alexa and Siri are my best friends..')
    elif 'Bye' in e.get():
        engine.say("")
        engine.runAndWait()
        txt.insert(END, "\n" + 'BOT--> bye have a good day...!')
    elif "ok bye" in e.get():
        engine.say("Bye,it was great talking to you...!")
        engine.runAndWait()
        txt.insert(END, "\n" + 'BOT--> Bye,it was great talking to you...!')
    elif "what can you do" in e.get():
        txt.insert(END, "\n" + 'BOT--> I can help you with any kind of stuff...')
        engine.say("I can help you with any kind of stuff")
        engine.runAndWait()
    elif 'open google' in e.get():
        txt.insert(END, "\n" + 'BOT--> Opening google...')
        kit.search('https://www.google.com')
        engine.say("Opening Google")
        engine.runAndWait()

    elif command1 in e.get():
        txt.insert(END, "\n" + "BOT --> Here is what I found")
        engine.say("Here is what i found")
        engine.runAndWait()
        kit.search(e.get())

    # elif msg in e.get():
    #     txt.insert(END, "\n" + "BOT --> Playing on Youtube")
    #     engine.say("Playing...")
    #     engine.runAndWait()
    #     kit.watch_tutorial_in_English()

    else:
        txt.insert(END, "\n" + "BOT --> Sorry i didn't get you")
        engine.say("Sorry i didn't get you")
        engine.runAndWait()

    e.delete(0, END)


txt = Text(rout, font='times 15 italic', width=70, bg='black', fg='white', bd=1, height=50)
txt.place(x=0, y=40)

e = Entry(rout, width=40, relief='raise', bd=2, font='times 20 bold')
e.place(x=720, y=80, height=40)

bt = Button(rout, text='SEND👉', bd=5, command=send, font='times 15 bold', bg = 'green')
bt.place(x=720, y=120, height=50)

bt1 = Button(rout, text='Exit process', bd=4, command=rout.quit, font='times 15 bold',bg = 'red')
bt1.place(x=720, y=200, height=50)

rout.mainloop()
