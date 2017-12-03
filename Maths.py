import tkinter as Tk
# Import Statements
from tkinter import messagebox
from tkinter import *
# Tkinter GUI creating library
import sys
from PIL import ImageTk, Image
# from photo image library import Tkinter image and image manipulation
from pygame import mixer
# Import pygame mixer library to play audio
import json
# library to decode json into python dictionary
from random import randint, shuffle
# Library to produce random integers and shuffle lists
# Library to create system dialogs

root = Tk()
# Set root to main tkinter window
root.minsize(width=666, height=666)
# Specify minimum size for root window
root.title("Revision")
# Set the title at top of the window

sound = True
# Variable to allow the user to disable sound


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
    englishInit=Tk()
    englishInit.geometry("800x400")
    def quiz():
        mat = Tk()
        mat.geometry("800x400")
        mat.title("English Quiz")
        mat.configure(bg="red")
        global score,count
        score=0
        count=0
        def ask_question():
            # get globals
            qq = get_questions("master/App/english.json")
            # retrive questions from json parcer with inputed json files
            eh1 = Label(mat, text="Question " + str(count+1), font="40")
            eh1.pack()
            score_readout = Label(mat, text="Score: " + str(score) + "/" + str(count), font="25")
            score_readout.pack()
            question_label = Label(mat, text=qq[4], font="30")
            question_label.pack()

            def correct():
                global score, count
                mixer.init(22050, -8, 4, 65536)
                mixer.music.load('master/App/rr.ogg')
                mixer.music.play(0)
                score = score + 1
                count = count + 1
                unpack_all()
                if count <= 11:
                    ask_question()
                else:
                    end_score = str(score) + " / " + str(10)
                    messagebox.showinfo("Score", "Your Score Was: %s" % end_score)
                    mat.destroy()

            def incorrect():
                global count, score
                mixer.init(22050, -8, 4, 65536)
                mixer.music.load('master/App/ww.ogg')
                mixer.music.play(0)
                count = count + 1
                unpack_all()
                if count < 10:
                    ask_question()
                else:
                    end_score = str(score)+"/"+ str(count)
                    score = 0
                    count = 0
                    messagebox.showinfo("Score", "Your Score Was: "+  str(score)+" Out of 12")
                    mat.destroy()
            def unpack_all():
                for mat_b in bttns:
                    mat_b.pack_forget()
                score_readout.pack_forget()
                eh1.pack_forget()
                question_label.pack_forget()
            mat_b1 = Button(mat, text=qq[0], command=correct,width=15,height=3)
            mat_b2 = Button(mat, text=qq[1], command=incorrect,width=15,height=3)
            mat_b3 = Button(mat, text=qq[2], command=incorrect,width=15,height=3)
            mat_b4 = Button(mat, text=qq[3], command=incorrect,width=15,height=3)
            bttns = [mat_b1, mat_b2, mat_b3, mat_b4]
            shuffle(bttns)
            for mat_ in bttns:
                mat_.pack()
        ask_question()
        mat.mainloop()
    englishInit.configure(background='Red')
    TitleLabel=Label(englishInit,text="Welcome to English!", bg="Red",font=(None,30),fg="Blue")
    TitleLabel.grid(row=0,column=0)
    RevisionOpener=Button(englishInit,text="Revision",bg='blue',width=10,height=3,font=(None,20),pady=5,padx=5)
    RevisionOpener.grid(row=1,column=0)
    QuizOpener=Button(englishInit,text="Quiz",command=quiz,bg='blue',width=10,height=3,font=(None,20),padx=5,pady=5)
    QuizOpener.grid(row=1,column=1)
    englishInit.mainloop()


def science():

    def quiz():
        mat = Tk()
        global count, score
        score=0
        count=0
        mat.geometry("800x400")
        mat.title("Science Quiz")

        def ask_question():
            global score, count
            qq = get_questions("master/App/jamesscience.json")
            eh1 = Label(mat, text="Question " + str(count+1), font="40")
            eh1.pack()
            score_readout = Label(mat, text="Score: " + str(score) + "/" + str(count), font="25")
            score_readout.pack()
            question_label = Label(mat, text=qq[4], font="30")
            question_label.pack()

            def correct():
                global score, count
                mixer.init(22050, -8, 4, 65536)
                mixer.music.load('master/App/rr.ogg')
                mixer.music.play(0)
                score = score + 1
                count = count + 1
                unpack_all()
                if count <= 11:
                    ask_question()
                else:
                    end_score = str(score) + " / " + "12"
                    messagebox.showinfo("Score", "Your Score Was: %s" % end_score)
                    mat.destroy()

            def incorrect():
                global count, score
                mixer.init(22050, -8, 4, 65536)
                mixer.music.load('master/App/ww.ogg')
                mixer.music.play(0)
                count = count + 1
                unpack_all()
                if count < 11:
                    ask_question()
                else:
                    end_score = str(score)+"/"+"10"
                    messagebox.showinfo("Score", "Your Score Was: %s" % score+"Out of 10")
                    score = 0
                    count = 0
                    end_score = 0
                    mat.destroy()

            def unpack_all():
                for mat_b in bttns:
                    mat_b.pack_forget()
                score_readout.pack_forget()
                eh1.pack_forget()
                question_label.pack_forget()
            mat_b1 = Button(mat, text=qq[0], command=correct)
            mat_b2 = Button(mat, text=qq[1], command=incorrect)
            mat_b3 = Button(mat, text=qq[2], command=incorrect)
            mat_b4 = Button(mat, text=qq[3], command=incorrect)
            bttns = [mat_b1, mat_b2, mat_b3, mat_b4]
            shuffle(bttns)
            for mat_ in bttns:
                mat_.pack()
        ask_question()
        mat.mainloop()

    quiz()


def math():

    def quiz():
        mat = Tk()
        global count, score
        score=0
        count=0
        mat.geometry("800x400")
        mat.title("Maths Quiz")

        def ask_question():
            global score, count
            qq = get_questions("master/App/jamesmaths.json")
            eh1 = Label(mat, text="Question " + str(count+1), font="40")
            eh1.pack()
            score_readout = Label(mat, text="Score: " + str(score) + "/" + str(count), font="25")
            score_readout.pack()
            question_label = Label(mat, text=qq[4], font="30")
            question_label.pack()

            def correct():
                global score, count
                mixer.init(22050, -8, 4, 65536)
                mixer.music.load('master/App/rr.ogg')
                mixer.music.play(0)
                score = score + 1
                count = count + 1
                unpack_all()
                if count <= 11:
                    ask_question()
                else:
                    end_score = str(score) + " / " + str(10)
                    messagebox.showinfo("Score", "Your Score Was: %s" % end_score)
                    mat.destroy()
                    
            def incorrect():
                global count, score
                mixer.init(22050, -8, 4, 65536)
                mixer.music.load('master/App/ww.ogg')
                mixer.music.play(0)
                count = count + 1
                unpack_all()
                if count < 11:
                    ask_question()
                else:
                    end_score = str(score)+"/"+"10"
                    messagebox.showinfo("Score", "Your Score Was: %s" % score+"Out of 10")
                    score = 0
                    count = 0
                    end_score = 0
                    mat.destroy()

            def unpack_all():
                for mat_b in bttns:
                    mat_b.pack_forget()
                score_readout.pack_forget()
                eh1.pack_forget()
                question_label.pack_forget()
            mat_b1 = Button(mat, text=qq[0], command=correct)
            mat_b2 = Button(mat, text=qq[1], command=incorrect)
            mat_b3 = Button(mat, text=qq[2], command=incorrect)
            mat_b4 = Button(mat, text=qq[3], command=incorrect)
            bttns = [mat_b1, mat_b2, mat_b3, mat_b4]
            shuffle(bttns)
            for mat_ in bttns:
                mat_.pack()
        ask_question()
        mat.mainloop()

    quiz()



menu = Menu(root)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="Credits")
# filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=sys.exit)
menu.add_cascade(label="File", menu=filemenu)
root.config(menu=menu)

h1 = Label(root, text="Revision", font="78")
h1.pack()
logo = ImageTk.PhotoImage(Image.open("master/App/logo.png"))
# logo2 = ImageTk.PhotoImage(Image.open("big_1489974512_image.jpg"))
# root.config(image=logo2)
panel = Label(root, image=logo)
panel.pack(side="bottom", fill="y", expand="yes")
bt1 = Button(root, text="English", bg="blue", command=english)
bt1.pack()
bt2 = Button(root, text="Maths", bg="blue", command=math)
bt2.pack()
bt3 = Button(root, text="Science", bg="blue", command=science)
bt3.pack()
h2 = Label(root, text="(c) Council Of Ricks 2017", font="30")
h2.pack()
score=0
count=0
root.mainloop()