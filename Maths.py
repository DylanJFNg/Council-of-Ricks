import tkinter as Tk
from tkinter import *
import sys
import os
import json
from pprint import pprint
from random import randint, shuffle
from builtins import str

# Tkinter GUI creating library
import PIL
from PIL import ImageTk, Image
# from photo image library import Tkinter image and image manipulation
from pygame import mixer
# Import pygame mixer library to play audio
import json
# library to decode json into python dictionary
import os
# Library to communicate with operating system
from random import randint, shuffle
# Library to produce random integers and shuffle lists
import platform
# Library to tell python what OS you are using
from tkinter import messagebox
# Library to create system dialogs:
root = Tk()
# Set root to main tkinter window
root.minsize(width=666, height=666)
# Specify minimum size for root window
root.title("Revision")
# Set the title at top of the window




def get_questions(json_file):
    file_open = open(json_file)
    # Opens specified JSON file for reading
    json_raw = file_open.read()
    # Reads JSON file as a string
    json_data = json.loads(json_raw)
    # Decodes JSON data as a python dictionary from a string
    index = json_data['index']
    # Gets index of how many questions are in JSON file
    question_selector = json_data[str(randint(1, index))]
    # Randomly selects interger between 1 and the number specified in the index list from JSON
    final_question = [question_selector['a'], question_selector['b'], question_selector['c'], question_selector['d'], question_selector['q']]
    # Creates a list of extracted json answers
    return final_question
    # Returns the question as a list to the script which called the function

# function to retrive random question from JSON file
# Usage get_questions(json_file_to_look_in)


"""
For simplicity we have split the tkinter sub-windows into
definitions so you can call them by pressing the button in the main window
activates a defined function with 

function_name(parameters_go_here)
"""


def english():
    def quiz():
        eng = Tk()
        score = 0
        count = 0
        eng.geometry("400x400")
        eng.title("English Quiz")
        def set_button_names(command):
            if command == "set":
                eng_b1 = Button(eng, text=qq[0])
                eng_b2 = Button(eng, text=qq[1])
                eng_b3 = Button(eng, text=qq[2])
                eng_b4 = Button(eng, text=qq[3])
                bttns = [eng_b1, eng_b2, eng_b3, eng_b4]
                return bttns
        def place_buttons():
            bttns = set_button_names("set")
            shuffle(bttns)
            for eng_ in bttns:
                eng_.pack()
            count=count+1
        while count < 11:
            # This "while" statement will close the window once you have
            # answered 10 questions on english
            qq = get_questions("master/App/english.json")
            eh1 = Label(eng, text="Question " + str(count+1), font="40")
            eh1.pack()
            score_readout = Label(eng, text="Score: " + str(score) + "/" + str(count), font="25")
            score_readout.pack()
            question_label = Label(eng, text=qq[4], font="30")
            question_label.pack()
            place_buttons()
            eng.mainloop()
    quiz()
    messagebox.showinfo("Score", "Your Score Was: %s")


def InitMaths():      
    def BackToRoot():
        python = sys.executable
        os.execl(python, python, * sys.argv)
    global Realwindow
    Realwindow=Tk()
    Realwindow.title("Mathematics Department")
    Realwindow.geometry("400x200")
    Realwindow.configure(background='Dark Blue')
    widget = Label(Realwindow, text= 'Do you want revision notes or questions?',bg='Light Blue')
    widget2= Button(Realwindow, text='Revision notes',bg='Cyan',fg='Red',command=Revision)
    widget3= Button(Realwindow, text='Randomly selected questions',bg='Cyan',fg='Red',command=MathsQuestions)
    widget.pack()
    widget2.pack()
    widget3.pack()
    backButton=Button(Realwindow,text="Back",bg='Cyan',fg='Red',command=BackToRoot)
    backButton.pack()
    Realwindow.mainloop()
def Revision():
    Realwindow.destroy()
    window3=Tk()
    window3.title("Revision")
    window3.geometry("1000x800")
    window3.configure(background='Dark Blue')
    def back():
        window3.destroy()
        InitMaths()
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

     
    Label1=Label(window3,text="Which mathematics subject do you want?",bg='cyan')
    AnglesButton=Button(window3,text="Angles",command=ReadAngles,bg='cyan')
    TrianglesButton=Button(window3,text="Triangles and trigonometrical ratios",command=ReadTriangles,bg='cyan')
    IndicesButton=Button(window3,text="Indices",command=ReadIndices,bg='cyan')
    SequencesButton=Button(window3,text="Sequences",command=ReadSequences,bg='cyan')
    PrimesButton=Button(window3,text="Prime Numbers",command=ReadPrime,bg='cyan')
    BackButton=Button(window3,text="Back",command=back,bg='Black',fg='White')
    Label1.pack()
    IndicesButton.pack()
    SequencesButton.pack()
    PrimesButton.pack()
    AnglesButton.pack()
    TrianglesButton.pack()
    BackButton.pack()
    window3.mainloop()
def MathsQuestions():
    Realwindow.destroy()
    Index1 = open("Resources/Maths.json","r")
    JsonIndex= json.load(Index1)
    window2= Tk()
    window2.title("Maths questions")
    window2.geometry("700x700")
    window2.configure(background='Dark Blue')
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
        InitMaths()
        window2.destroy()
    def Incorrect():
        from tkinter import messagebox
        messagebox.showinfo(title="Incorrect answer", message= "That's the wrong answer. Try again.")
    

    questions=get_MathsQuestions()
    MathsLabel=Label(window2,text=questions[4])
    MathsLabel.pack()
    def set_Maths_button_names(command):
        if command == "set":
            Maths_b1 = Button(window2, text=questions[0],command=Correct)
            Maths_b2 = Button(window2, text=questions[1],command=Incorrect)
            Maths_b3 = Button(window2, text=questions[2],command=Incorrect)
            Maths_b4 = Button(window2, text=questions[3],command=Incorrect)
            bttns = [Maths_b1, Maths_b2, Maths_b3, Maths_b4]
            return bttns
    def ButtonPlacements():
        def place_buttons():
            bttns = set_Maths_button_names("set")
            shuffle(bttns)
            for window2_ in bttns:
                window2_.pack()
        place_buttons()
        window2.mainloop()
    ButtonPlacements()
h1 = Label(root, text="Revision", font="78")
h1.pack()
logo = ImageTk.PhotoImage(Image.open("master/App/logo.png"))
panel = Label(root, image=logo)
panel.pack(side="bottom", fill="y", expand="yes")
bt1 = Button(root, text="English", bg="blue", command=english)
bt1.pack()
bt2 = Button(root, text="Maths", bg="blue",command=InitMaths)
bt2.pack()
bt3 = Button(root, text="Science", bg="blue")
bt3.pack()
h2 = Label(root, text="(c) Council Of Ricks 2017", font="30")
h2.pack()
root.mainloop()
sound = True 

        






  