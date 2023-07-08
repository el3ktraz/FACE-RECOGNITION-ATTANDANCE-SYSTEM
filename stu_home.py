import os  # accessing the os functions
import check_camera
import Capture_Image

import Recognize
from tkinter import * 
import tkinter as tk
import threading



def rfaces_call():
	tkStatus.set("Recognizing Faces...")
	status_label.update()
	Recognize.recognize_attendence()
	tkStatus.set("Faces Recognized.")
	status_label.update()

def RecognizeFaces():
	t4=threading.Thread(target=rfaces_call,daemon=True)
	t4.start()



root = Tk()  
root.title("Contactless Attendance System")
tkID = tk.StringVar()
tkName = tk.StringVar()
tkEmail = tk.StringVar()  
tkStatus = tk.StringVar()      
 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (400 / 2))  # Adjust the window width as needed
y_coordinate = int((screen_height / 2) - (300 / 2))  # Adjust the window height as needed

# Set the window position to the center of the screen
root.geometry(f"400x400+{x_coordinate}+{y_coordinate}")





btn4 = tk.Button(
    root,
    text='RECOGNIZE FACES',
    command=RecognizeFaces,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn4.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=6,
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


btn6 = tk.Button(
    root,
    text='EXIT',
    command=root.destroy,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn6.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=8,
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

status_label = tk.Label(
    root,
    textvariable=tkStatus,
    bg='#eeeeee',
    anchor=tk.W,
    justify=tk.LEFT,
    relief=tk.FLAT,
    wraplength=350,
    )
status_label.grid(
    padx=12,
    pady=(0, 12),
    ipadx=0,
    ipady=1,
    row=9,
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )
 
 
 
root.mainloop()

