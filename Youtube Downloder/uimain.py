from tkinter import *
from tkinter import ttk # used to make frames and arrange items in frams
from tkinter.font import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import os, sys, subprocess, shutil, glob, os.path, csv
    



#main window
main = Tk()
main.title('AV Download')
main.geometry('900x900')
main.resizable(False, True)
main['bg']='darkgray'

#def
def info():
    blank.delete(0.0, END)  # this to clear the text book every time pushing the Info button
    from pafy import new
    url=link.get()
    av = new(url)
    blank.insert(END, "Title: " + av._title + "\n" + "Author: " + av._author + "\n" + "Duration: " + str(av._duration) + "\n" + "Length: " + str(av._length) + "\n" + "Publish Date: " + str(av._published) +"\n" + "View count: " + str(av._viewcount))
    quality = av.streams
    for i in quality:
        blank.insert(END, "\nAvailable Video Streams: " + str(i))
    stream = av.audiostreams
    for i in stream:
        blank.insert(END, "\nAvailable Audio Streams: " + str(i))

            
def vid():
    from pafy import new
    url=link.get()
    av = new(url)
    best = av.getbest()
    #best.download(filepath = filedialog.askdirectory()) # this one help to select the directory of download
    best.download(filepath = filedialog.asksaveasfilename()) # this one help in select the directory and to change the file name as well but not the extention
    
    
    
def aud():
    from pafy import new
    url=link.get()
    av = new(url)
    best = av.getbestaudio()
    #best.download(filepath = filedialog.askdirectory())
    best.download(filepath = filedialog.asksaveasfilename())
    
# Frames
# creating main frame that take all window and another one to arrange the buttons in it
mainfram = ttk.Frame(main, padding = "5 5 12 12", relief=GROOVE, borderwidth=2)
mainfram.grid(row= 0, column= 0, sticky=(N, S, W, E))
frame1 = ttk.Frame(mainfram, padding = "5 5 10 10", relief= GROOVE,borderwidth=3)
frame1.grid(row = 1, column= 0, sticky=(N, S, W, E))
# relief "8": must be flat, groove, raised, ridge, solid, or sunken
# borderwidth for the boarder thickness
frame2 = ttk.Frame(mainfram, padding = "5 5 10 10", relief= GROOVE,borderwidth=3)
#frame2.grid(row = 2, column= 0, sticky=(N, S, W, E))
frame2.grid(row = 5, column= 0, sticky =(E,W)) # when we remove sticky the wedget alligned to center automaticaly 
frame3 = ttk.Frame(mainfram, padding = "5 5 10 10", relief= GROOVE,borderwidth=3)
frame3.grid(row = 6, column= 0, sticky = (E,W)) # E & W let frame take the full width of main windows
frame4 = ttk.Frame(mainfram, padding = "5 5 10 10", relief= GROOVE,borderwidth=3)
frame4.grid(row = 3, column= 0, sticky = (E,W)) 


#lables & Butuns 
Label(frame1, text= "This Program help you to download videos & audios from Youtub", fg='blue').grid(row=1)
Label(frame2, text= "Please slect Video or Audio").grid(row=0, column = 0, padx =5, ipadx = 250)
Button(frame3, height= 1, width= 2, text='Info', font = BOLD, command = info).grid(row=2, column=0, padx=5, ipadx = 100)
Button(frame3, height= 1, width= 2, text='Video', font = BOLD, command = vid).grid(row=2, column=1, padx=5, ipadx = 100)
Button(frame3, height= 1, width= 2, text='Audio', font = BOLD, command = aud).grid(row=2, column=2, padx= 5,ipadx = 100)
Label(frame4, text= "Please add link below & Enter").grid(row=0, column = 0, padx=5, pady=5,)
link = Entry(frame4)
link.grid(row=1, column = 0, padx=5, pady=5, ipady = 30, ipadx = 250)
Label(frame4, text= "Video information").grid(row=2, column = 0, padx=5, pady=5,)
blank= Text(frame4, height = 4, width = 8)
blank.grid(row=3, column = 0, padx=0, pady=0, ipady = 150, ipadx = 350)


    
mainloop()

# inhansment in this program should include
# download monetring (development bar)
# convert audio to MP3 directly
# message to indecate that download is done 