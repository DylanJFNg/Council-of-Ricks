# Import Statements
from Tkinter import *
# Tkinter GUI creating library
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
import tkMessageBox
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
score = 0
count = 0


def english():
    global score
    global count

    def quiz():
        eng = Tk()
        eng.geometry("400x400")
        eng.title("English Quiz")
        while count < 11:
            # This "while" statement will close the window once you have
            # answered 10 questions on english
            qq = get_questions("english.json")
            eh1 = Label(eng, text="Question " + str(count+1), font="40")
            eh1.pack()
            score_readout = Label(eng, text="Score: " + str(score) + "/" + str(count), font="25")
            score_readout.pack()
            question_label = Label(eng, text=qq[4], font="30")
            question_label.pack()

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
            place_buttons()
            eng.mainloop()
    quiz()
    tkMessageBox.showinfo("Score", "Your Score Was: %s" % "you are a faliur")


def math():
    def quiz():
        mat = Tk()
        global count, score
        mat.geometry("400x400")
        mat.title("Math Quiz")
        while count < 11:
            # This "while" statement will close the window once you have
            # answered 10 questions on maths
            def ask_question():
                global score, question_text, count
                qq = get_questions("jamesmaths.json")
                eh1 = Label(mat, text="Question " + str(count+1), font="40")
                eh1.pack()
                score_readout = Label(mat, text="Score: " + str(score) + "/" + str(count), font="25")
                score_readout.pack()
                question_label = Label(mat, text=qq[4], font="30")
                question_label.pack()

                def correct():
                    global score, count
                    score = score + 1
                    count = count + 1
                    unpack_all()
                    ask_question()

                def incorrect():
                    global count, score
                    count = count + 1
                    unpack_all()
                    ask_question()

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
        mat.destroy()
        tkMessageBox.showinfo("Score", "Your Score Was: %s" % "you are a faliur")
    quiz()


h1 = Label(root, text="Revision", font="78")
h1.pack()
logo = ImageTk.PhotoImage(Image.open("logo.png"))
panel = Label(root, image=logo)
panel.pack(side="bottom", fill="y", expand="yes")
bt1 = Button(root, text="English", bg="blue", command=english)
bt1.pack()
bt2 = Button(root, text="Maths", bg="blue", command=math)
bt2.pack()
bt3 = Button(root, text="Science", bg="blue")
bt3.pack()
h2 = Label(root, text="(c) Council Of Ricks 2017", font="30")
h2.pack()

root.mainloop()
