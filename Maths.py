import tkinter as Tk
from tkinter import *


window= Tk()
window.title("Mathematics department")
window.geometry("400x200")

def openquestions():
    window.destroy()
    import Maths_questions
    

widget = Label(window, text= 'Do you want revision notes or questions?')
widget2= Button(window, text='Revision notes')
widget3= Button(window, text='Randomly selected questions',command=openquestions)
widget.pack()
widget2.pack()
widget3.pack()
window.mainloop()



  
