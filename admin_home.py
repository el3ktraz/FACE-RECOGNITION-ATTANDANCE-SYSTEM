import os  # accessing the os functions
import check_camera
import Capture_Image

import Recognize
from tkinter import * 
import tkinter as tk
import threading



# creating the title bar function


# ---------------------------------------------------------
# calling the camera test function from check camera.py file

def cc_call():
	tkStatus.set("Accessing Camera...")
	status_label.update()
	check_camera.camer()
	tkStatus.set("")
	status_label.update()

def checkCamera():
	t1=threading.Thread(target=cc_call,daemon=True)
	t1.start()
	
def autom_call():
	tkStatus.set("Sending Mail...")
	status_label.update()
	os.system("py automail.py")
	tkStatus.set("Mail Sent")
	status_label.update()

def autom():
	t5=threading.Thread(target=autom_call,daemon=True)
	t5.start()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def cfaces_call():
    tkStatus.set("Capturing Faces...")
    status_label.update()
    try:
        Capture_Image.takeImages(str(tkName.get()))
        tkStatus.set("Faces Captured")
        id_label.update()
        tkName.set("")
        name_label.update()
    except Exception as e:
        if (tkID.get().isnumeric()==False):
            tkStatus.set("Enter valid user id")
            status_label.update()
        else:
            tkStatus.set("Enter valid user email")
            status_label.update()


def CaptureFaces():
	t2=threading.Thread(target=cfaces_call,daemon=True)
	t2.start()

# -----------------------------------------------------------------
# calling the train images from train_images.py file

def timages_call():
	tkStatus.set("Showing Attendance...")
	status_label.update()
	os.system("streamlit run app.py")
	tkStatus.set("Attendance Displayed")
	status_label.update()

	

def Trainimages():
	t3=threading.Thread(target=timages_call,daemon=True)
	t3.start()
	


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file
def rfaces_call():
	tkStatus.set("Recognizing Faces...")
	status_label.update()
	Recognize.recognize_attendence()
	tkStatus.set("Faces Recognized.")
	status_label.update()

def RecognizeFaces():
	t4=threading.Thread(target=rfaces_call,daemon=True)
	t4.start()


# ---------------main driver ------------------
# create a tkinter window
root = Tk()  
root.title("Contactless Attendance System")
tkID = tk.StringVar()
tkName = tk.StringVar()
tkEmail = tk.StringVar()  
tkStatus = tk.StringVar()      
 
# Open window having dimension 100x100
#root.geometry('100x100') 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (400 / 2))  # Adjust the window width as needed
y_coordinate = int((screen_height / 2) - (300 / 2))  # Adjust the window height as needed

# Set the window position to the center of the screen
root.geometry(f"400x400+{x_coordinate}+{y_coordinate}")
# Create a Button

btn1 = tk.Button(
    root,
    text='CHECK CAMERA',
    command=checkCamera,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn1.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=0,
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )



name_label = tk.Label(root,
        text='Enter Name:', bg='#eeeeee',
        anchor=tk.W)
name_label.grid(
    padx=12,
    pady=(8, 0),
    ipadx=0,
    ipady=1,
    row=2,
    column=0,
    columnspan=1,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

name_entry = tk.Entry(root, textvariable=tkName,
                           bg='#fff', exportselection=0,
                           relief=tk.FLAT)
name_entry.grid(
    padx=15,
    pady=6,
    ipadx=8,
    ipady=8,
    row=2,
    column=1,
    columnspan=3,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )




btn2 = tk.Button(
    root,
    text='CAPTURE FACES',
    command=CaptureFaces,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn2.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=4,
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


btn3 = tk.Button(
    root,
    text='SHOW ATTENDANCE',
    command=Trainimages,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn3.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=5,
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


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


btn5 = tk.Button(
    root,
    text='AUTO MAIL',
    command=autom,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn5.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=7,
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
 
# Set the position of button on the top of window.      
 
root.mainloop()
#mainMenu()
