import tkinter as Tk
from tkinter import *
import sys
import os
import json
from pprint import pprint
from random import randint, shuffle
from builtins import str
window= Tk()
window.title("Mathematics department")
window.geometry("400x200")

def InitMaths():
    widget = Label(window, text= 'Do you want revision notes or questions?')
    widget2= Button(window, text='Revision notes',command=Revision)
    widget3= Button(window, text='Randomly selected questions',command=MathsQuestions)
    widget.pack()
    widget2.pack()
    widget3.pack()
    window.mainloop()


def Revision():
    window.destroy()
    window3=Tk()
    window3.title("Revision")
    window3.geometry("1000x800")

    
    def back():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    TrianglesText=open("Resources\TrianglesAndTrigonometricRatios.txt","r")
    SequencesText=open("Resources\SequencesRevision.txt","r")
    AnglesText=open("Resources\AnglesRevision.txt","r")
    IndicesText=open("Resources\IndicesRevision.txt","r")
    PrimeText=open("Resources\PrimeNumbers.txt","r")

    Triangles=TrianglesText.read()
    Label2=Label(window3,text=Triangles,font=("none",10))

    Angles=AnglesText.read()
    Label3=Label(window3,text=Angles,font=("none",10))

    Sequences=SequencesText.read()
    Label4=Label(window3,text=Sequences,font=("none",10))

    Indices=IndicesText.read()
    Label5=Label(window3,text=Indices,font=("none",10))

    Prime=PrimeText.read()
    Label6=Label(window3,text=Prime,font=("none",10))




    def ReadTriangles():
        def back2():
            Label2.pack_forget()
            Label1.pack()
            IndicesButton.pack()
            SequencesButton.pack()
            PrimesButton.pack()
            AnglesButton.pack()
            TrianglesButton.pack()
            BackButton.pack()
            BackButton2.destroy()
            window3.mainloop()
        Label2.pack()
        Label1.pack_forget()
        IndicesButton.pack_forget()
        SequencesButton.pack_forget()
        PrimesButton.pack_forget()
        AnglesButton.pack_forget()
        TrianglesButton.pack_forget()
        BackButton.pack_forget()
        BackButton2=Button(window3,text="Back",command=back2)
        BackButton2.pack()
        window3.mainloop()
    def ReadAngles():
        def back3():
            Label3.pack_forget()
            Label1.pack()
            IndicesButton.pack()
            SequencesButton.pack()
            PrimesButton.pack()
            AnglesButton.pack()
            TrianglesButton.pack()
            BackButton.pack()
            BackButton2.destroy()
            window3.mainloop()
        Label3.pack()
        Label1.pack_forget()
        AnglesButton.pack_forget()
        TrianglesButton.pack_forget()
        IndicesButton.pack_forget()
        SequencesButton.pack_forget()
        PrimesButton.pack_forget()
        BackButton.pack_forget()
        BackButton2=Button(window3,text="Back",command=back3)
        BackButton2.pack()
        window3.mainloop()
    def ReadIndices():
        def back4():
            Label5.pack_forget()
            Label1.pack()
            IndicesButton.pack()
            SequencesButton.pack()
            PrimesButton.pack()
            AnglesButton.pack()
            TrianglesButton.pack()
            BackButton.pack()
            BackButton2.destroy()
            window3.mainloop()
        Label5.pack()
        Label1.pack_forget()
        AnglesButton.pack_forget()
        TrianglesButton.pack_forget()
        IndicesButton.pack_forget()
        SequencesButton.pack_forget()
        PrimesButton.pack_forget()
        BackButton.pack_forget()
        BackButton2=Button(window3,text="Back",command=back4)
        BackButton2.pack()
        window3.mainloop()  
    def ReadSequences():
        def back5():
            Label4.pack_forget()
            Label1.pack()
            IndicesButton.pack()
            SequencesButton.pack()
            PrimesButton.pack()
            AnglesButton.pack()
            TrianglesButton.pack()
            BackButton.pack()
            BackButton2.destroy()
            window3.mainloop()
        Label4.pack()
        Label1.pack_forget()
        AnglesButton.pack_forget()
        TrianglesButton.pack_forget()
        IndicesButton.pack_forget()
        SequencesButton.pack_forget()
        PrimesButton.pack_forget()
        BackButton.pack_forget()
        BackButton2=Button(window3,text="Back",command=back5)
        BackButton2.pack()
        window3.mainloop() 
    
    def ReadPrime():
        def back6():
            Label6.pack_forget()
            Label1.pack()
            IndicesButton.pack()
            SequencesButton.pack()
            PrimesButton.pack()
            AnglesButton.pack()
            TrianglesButton.pack()
            BackButton.pack()
            BackButton2.destroy()
            window3.mainloop()
        Label6.pack()
        Label1.pack_forget()
        AnglesButton.pack_forget()
        TrianglesButton.pack_forget()
        IndicesButton.pack_forget()
        SequencesButton.pack_forget()
        PrimesButton.pack_forget()
        BackButton.pack_forget()
        BackButton2=Button(window3,text="Back",command=back6)
        BackButton2.pack()
        window3.mainloop() 
    
     
    Label1=Label(window3,text="Which mathematics subject do you want?")
    AnglesButton=Button(window3,text="Angles",command=ReadAngles)
    TrianglesButton=Button(window3,text="Triangles and trigonometrical ratios",command=ReadTriangles)
    IndicesButton=Button(window3,text="Indices",command=ReadIndices)
    SequencesButton=Button(window3,text="Sequences",command=ReadSequences)
    PrimesButton=Button(window3,text="Prime Numbers",command=ReadPrime)
    BackButton=Button(window3,text="Back",command=back)
    Label1.pack()
    IndicesButton.pack()
    SequencesButton.pack()
    PrimesButton.pack()
    AnglesButton.pack()
    TrianglesButton.pack()
    BackButton.pack()
    window3.mainloop()

def MathsQuestions():
    window.destroy()
    Index1 = open("Resources/Index.json","r")
    JsonIndex= json.load(Index1)

    window2= Tk()
    window2.title("Maths questions")
    window2.geometry("700x700")

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
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
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


InitMaths()
  
