from tkinter import *
from playsound import playsound
from gtts import gTTS

root=Tk()
root.title("Text-to-Speech Converter")
root.geometry("400x300+400+250")


def convert():
    message=entTxt.get()
    speech=gTTS(text=message,lang='en')
    speech.save('text_to_speech.mp3')
    playsound('text_to_speech.mp3')
    
    

def reset():
    entTxt.delete(0,END)
    entTxt.focus()
    


lblTxt=Label(root,text="Enter text",font=("Times New Roman",15))
entTxt=Entry(root,bd=4,font=("Times New Roman",15))
btnPlay=Button(root,text="PLAY",font=("Times New Roman",15,"bold"),bg = 'LightBlue',command=convert)
btnReset=Button(root,text="RESET",font=("Times New Roman",15,"bold"),bg = 'OrangeRed1',command=reset)
#
lblTxt.pack(pady=10)
entTxt.pack(pady=10)
btnPlay.pack(pady=10)
btnPlay.place(x=120,y=130)
btnReset.pack(pady=10)
btnReset.place(x=200,y=130)

root.mainloop()
