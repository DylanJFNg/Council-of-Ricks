import tkinter as Tk
from tkinter import *
 
window= Tk()
window.title("Maths department")
window.geometry("400x200")




widget = Label(window, text= 'Do you want revision notes or questions?')
widget2= Button(window, text='Revision notes')
widget3= Button(window, text='Questions')
widget.pack()
widget2.pack()
widget3.pack()
window.mainloop()

def quit_window(self):
    self.Q1()
    self.window.destroy()

  
