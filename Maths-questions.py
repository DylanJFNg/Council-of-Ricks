
import tkinter as Tk
from tkinter import *
import json
from pprint import pprint
global data



Index1 = open("Resources/Index.json","r")
JsonIndex= json.load(Index1)
question1=JsonIndex["Index"]["1"]["q"]


 
window2= Tk()
window2.title("Maths questions")
window2.geometry("400x400")

def Correct():
    from tkinter import messagebox
    messagebox.showinfo(title="You're right!", message="Well done! You got the answer correct!")

def Incorrect():
    from tkinter import messagebox
    messagebox.showinfo(title="Incorrect answer", message= "Wrong! Remember, 2 is a prime number. The other primes in the range 1-10 are 3,5,7. 4/10= 40%.")

text_file= open("Resources/Maths Questions.txt", "r")
text_file2= open("Resources/Possible answers.txt", "r")
text_file3= open("Resources/Possible answers 2.txt","r")
text_file4= open("Resources/Possible answers 3.txt","r")
text_file5= open("Resources/Possible answers 4.txt","r")
Lines= Label(window2,text=question1)
Button1= Button(window2,text=text_file2.read(6), command= Correct)
Button2= Button(window2,text=text_file3.read(6), command= Incorrect)
Button3= Button(window2,text=text_file4.read(6), command=Incorrect)
Button4= Button(window2,text=text_file5.read(6), command=Incorrect)
Lines.pack()
Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
window2.mainloop()
text_file.close()
text_file2.close()
text_file3.close()
text_file4.close()
text_file5.close()


    