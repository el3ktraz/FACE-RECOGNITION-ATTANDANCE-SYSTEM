import tkinter as tk
from tkinter import messagebox
import subprocess

def validate_login():
    admin_username = "test"
    admin_password = "pass"

    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == admin_username and entered_password == admin_password:
        messagebox.showinfo("Login Successful", "Welcome!")
        window.withdraw()
        subprocess.call(["python", "stu_home.py"])
        window.destroy()
        
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

window = tk.Tk()
window.title("Attendance Management System")


primary_color = "#3498db"
secondary_color = "#ffffff"
font_color = "#333333"
bg_color = "#f2f2f2"


entry_style = {"foreground": font_color, "background": secondary_color, "highlightbackground": primary_color, "highlightcolor": primary_color, "highlightthickness": 2, "relief": tk.FLAT}
label_style = {"foreground": font_color, "background": bg_color, "font": ("Arial", 12), "padx": 5, "pady": 5}
button_style = {"foreground": secondary_color, "background": primary_color, "font": ("Arial", 12), "padx": 10, "pady": 5, "relief": tk.RAISED}

window.configure(bg=bg_color)


window_width = 400
window_height = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
window.resizable(False, False)


heading_label = tk.Label(window, text="STUDENT LOGIN", font=("Arial", 16, "bold"))
heading_label.configure(**label_style)
heading_label.pack(pady=10)


username_label = tk.Label(window, text="Username:", **label_style)
username_label.pack()
username_entry = tk.Entry(window, **entry_style)
username_entry.pack()

password_label = tk.Label(window, text="Password:", **label_style)
password_label.pack()
password_entry = tk.Entry(window, show="*", **entry_style)
password_entry.pack()


login_button = tk.Button(window, text="Login", command=validate_login, **button_style)
login_button.pack(pady=10)


window.mainloop()
