# this example for calculator using grid
# It is copy past project but make changes in its outlook 


from tkinter import *
from math import *
from tkinter import ttk # used to make frames and arrange items in frams
from tkinter.font import BOLD
main = Tk()
main.title('CALCULATOR')

# creating main frame that take all window and another one to arrange the buttons in it
mainfram = ttk.Frame(main, padding = "5 5 12 12", relief=GROOVE, borderwidth=2)
mainfram.grid(row= 0, column= 0, sticky=(N, S, W, E))
frame2 = ttk.Frame(mainfram, padding = "5 5 10 10", relief= GROOVE,borderwidth=2)
frame2.grid(row = 4, column= 1, sticky=(N, S, W, E))
# relief "8": must be flat, groove, raised, ridge, solid, or sunken 
# borderwidth for the boarder thickness

def add():
    blank.delete(0, END)
    Ans = float(num1.get()) + float(num2.get())
    blank.insert(0, Ans)
def sub():
    blank.delete(0, END)
    Ans = float(num1.get()) - float(num2.get())
    blank.insert(0, Ans)
def mult():
    blank.delete(0, END)
    Ans = float(num1.get()) * float(num2.get())
    blank.insert(0, Ans)
def div():
    blank.delete(0, END)
    Ans = float(num1.get()) / float(num2.get())
    blank.insert(0, Ans)
def clear():
    blank.delete(0, END)
    num2.delete(0, END)
    num1.delete(0, END)
def sq():
    blank.delete(0, END)
    Ans = float(num1.get()) * float(num1.get())
    blank.insert(0, Ans)

def sqrtt():
    blank.delete(0, END)
    h = float(num1.get())
    a = sqrt(h)
    Ans = (float(a))
    blank.insert(0, Ans)

main.geometry('615x400')
main.resizable(False, False) # to prevent resize of the main windows 
#main.maxsize = "320 x 280"
Label(mainfram, text = "Enter Num 1:").grid(row=0)
Label(mainfram, text = "Enter Num 2:").grid(row=1)
Label(mainfram, text = "The Answer is:").grid(row=2)


num1 = Entry(mainfram)
num2 = Entry(mainfram)
blank = Entry(mainfram)


num1.grid(row=0,column=1, padx=5, pady=5, ipadx= 20)
num2.grid(row=1, column=1, padx=5, pady=5, ipadx= 20)
blank.grid(row=2, column=1, padx=5, pady=5, ipadx= 20)



Button(frame2, height= 1, width= 2, text='+', font = BOLD, command=add).grid(row=4, column=0, padx=5, pady=5)
Button(frame2, height= 1, width= 2, text='-', font = BOLD, command=sub).grid(row=4, column=1, padx=5, pady=5)
Button(frame2, height= 1, width= 2, text='*', font = BOLD, command=mult).grid(row=4, column=2, padx=5, pady=5)
Button(frame2, height= 1, width= 2, text='/', font = BOLD, command=div).grid(row=6, column=0, padx=5, pady=5)
Button(frame2, height= 1, width= 2, text='^2', font = BOLD, command=sq).grid(row=6, column=1, padx=5, pady=5)
Button(frame2, height= 1, width= 2, text='Sq', font = BOLD, command=sqrtt).grid(row=6, column=2, padx=5, pady=5)
Button(frame2, height= 1, width= 3, text='Cle', font = BOLD, fg ="Red", bg = "Blue", command=clear).grid(row=7, column=1, padx=5, pady=5)
Button(frame2, height= 1, width= 3, text='Qut', font = BOLD, fg ="Red", bg = "Blue", command=main.destroy).grid(row=7, column=2, padx=5, pady=5)
# remove ipadx & ipady to make button appear more natural
# using height and width to make buttone same size 

mainloop()