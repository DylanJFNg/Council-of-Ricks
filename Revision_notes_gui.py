import sys
import os
import tkinter as Tk
from tkinter import *
window3=Tk()
window3.title("Revision")
window3.geometry("500x500")

def back():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    

Label1=Label(window3,text="Which mathematics subject do you want?")
AnglesButton=Button(window3,text="Angles")
TrianglesButton=Button(window3,text="Triangles and trigonometrical ratios")
IndicesButton=Button(window3,text="Indices")
SequencesButton=Button(window3,text="Sequences")
PrimesButton=Button(window3,text="Prime Numbers")
BackButton=Button(window3,text="Back",command=back)
Label1.pack()
IndicesButton.pack()
SequencesButton.pack()
PrimesButton.pack()
AnglesButton.pack()
TrianglesButton.pack()
BackButton.pack()
window3.mainloop()