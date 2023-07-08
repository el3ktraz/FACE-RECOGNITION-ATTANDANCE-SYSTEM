import tkinter as tk
import os

def open_admin():
    os.system("python admin.py")

def open_staff():
    os.system("python staff.py")

def open_student():
    os.system("python student.py")

window = tk.Tk()
window.title("Home")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 500
window_height = 300
window.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

primary_color = "#3498db"
secondary_color = "#ffffff"
font_color = "#333333"

heading_frame = tk.Frame(window, bg="white")
heading_frame.pack(pady=20)

heading_label = tk.Label(heading_frame, text="ATTENDANCE SYSTEM USING FACE RECOGNITION", font=("Arial", 14, "bold"), fg=font_color, bg="white")
heading_label.pack()

button_frame = tk.Frame(window, bg="white")
button_frame.pack(pady=20)

buttons = []
labels = ["Admin", "Staff", "Student"]

button_width = 15
button_height = 3

for i, label in enumerate(labels):
    button = tk.Button(button_frame, text=label, command=lambda l=label: open_file(l), bg=primary_color, fg=secondary_color, relief=tk.RAISED, width=button_width, height=button_height)
    button.grid(row=0, column=i, padx=10)

def open_file(label):
    if label == "Admin":
        open_admin()
    elif label == "Staff":
        open_staff()
    elif label == "Student":
        open_student()

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

subheading_frame = tk.Frame(window, bg="white")
subheading_frame.pack(pady=10)

project_label = tk.Label(subheading_frame, text="Project by:", font=("Arial", 12))
project_label.pack(side=tk.LEFT)

names_label = tk.Label(subheading_frame, text="Abhishek & Allan", font=("Arial", 12, "bold"))
names_label.pack(side=tk.LEFT)

window.mainloop()
