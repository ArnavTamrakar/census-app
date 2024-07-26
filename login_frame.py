import customtkinter as ctk
from tkinter import messagebox
import sqlite3

def show_warning_empty():
    messagebox.showwarning("Field Empty", "Cannot be left empty")

def show_warning_match():
    messagebox.showwarning("Password Mismatch", "Passwords do not match")

def create_login_frame(parent, open_register, open_homepage):
    def login_check():
        username = username_entry.get()
        password = password_entry.get()

        # checking if any of the field are left empty
        if username == '' or password == '':
            show_warning_empty()
        else:
            conn = sqlite3.connect('census.db')
            cursor = conn.execute('SELECT * FROM creds WHERE email=? AND password=?', (username, password))
            # checking if the entered username and password mateches with the one in database
            if cursor.fetchone():
                messagebox.showinfo(title="Welcome", message="Login Success")
                open_homepage()
            else:
                messagebox.showinfo(title="Wrong Details", message="Email or password wrong")

    frame = ctk.CTkFrame(parent, width=400, height=350, fg_color='white', border_color='black', border_width=2)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    frame.pack_propagate(False)

    title_label = ctk.CTkLabel(frame, text="Census 2025", font=ctk.CTkFont(size=36, weight="bold"))
    title_label.pack(pady=(20, 40))

    username_entry = ctk.CTkEntry(frame, placeholder_text="Email", width=300, height=40)
    username_entry.pack(pady=(0, 20))

    password_entry = ctk.CTkEntry(frame, placeholder_text="Password", show='*', width=300, height=40)
    password_entry.pack(pady=(0, 20))

    login_button = ctk.CTkButton(frame, text="Log in", font=ctk.CTkFont(size=20), width=300, height=40, command=login_check)
    login_button.pack(pady=(0, 20))

    register_label = ctk.CTkLabel(frame, text="Don't have an account? Register Now.", font=ctk.CTkFont(size=10), text_color="blue", cursor="hand2")
    register_label.pack()
    register_label.bind("<Button-1>", lambda e: open_register())

    return frame
