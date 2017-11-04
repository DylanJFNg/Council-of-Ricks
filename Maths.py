import tkinter as Tk
from tkinter import *
 
window= Tk()
window.title("Maths department")
window.geometry("400x400")





widget = Label(window, text= 'Do you want revision notes or questions?')
widget2= Button(window, text='Revision notes')
widget.pack()
widget.mainloop()
widget2.pack()
widget2.mainloop()


