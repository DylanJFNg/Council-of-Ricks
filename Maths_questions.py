import random
import tkinter as Tk
from tkinter import *
import json
from pprint import pprint
from random import randint, shuffle
from builtins import str


Index1 = open("Resources/Index.json","r")
JsonIndex= json.load(Index1)

count=0


window2= Tk()
window2.title("Maths questions")
window2.geometry("500x500")

def get_MathsQuestions():
    index = JsonIndex["Index"]  
    RealIndex = int(index)  
    tmp = str(randint(1,RealIndex))
    Real_question_selector = JsonIndex[tmp]   
    final_question = [Real_question_selector["a"], Real_question_selector["b"], Real_question_selector["c"], Real_question_selector["d"], Real_question_selector["q"]]
    return final_question

def Correct():
    from tkinter import messagebox
    messagebox.showinfo(title="You're right!", message="Well done! You got the answer correct!")
    window2.destroy()
    
def Incorrect():
    from tkinter import messagebox
    messagebox.showinfo(title="Incorrect answer", message= "That's the wrong answer. Try again.")


    
questions=get_MathsQuestions()


MathsQuestion_label=Label(window2, text=questions[4])
MathsQuestion_label.pack()
Button1= Button(window2,text=questions[0],command=Correct)
Button2= Button(window2,text=questions[1],command=Incorrect)
Button3= Button(window2,text=questions[2],command=Incorrect)
Button4= Button(window2,text=questions[3],command=Incorrect)
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
window2.mainloop()
    





    