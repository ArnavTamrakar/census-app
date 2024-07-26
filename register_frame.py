import customtkinter as ctk
from tkinter import messagebox
import sqlite3

# function to be called incase something is empty
def show_warning_empty():
    messagebox.showwarning("Field Empty", "Cannot be left empty")

#function to be called if password mismatch
def show_warning_match():
    messagebox.showwarning("Password Mismatch", "Passwords do not match")

def create_register_frame(parent, open_login):
    def reg():
        # Retrieve the value entered in the entry 
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        email = email_entry.get()
        password = pass_entry.get()
        repassword = pass_confirm_entry.get()

        # Check if any fields are left empty
        if firstname == '' or lastname == '' or email == '' or password == '' or repassword == '':
            # if empty show warning using the function that has been called earlier
            show_warning_empty()
        # Check if passwords match with eachother
        elif password != repassword:
            # If password mismatch show warning using function that has been called earlier
            show_warning_match()
        else:
            # If passwords match and all the required fields are filled, proceeds
            conn = sqlite3.connect('census.db')
            # Connecting to the database
            c = conn.cursor()

            # Creating the credentials table is it doesnt exist 
            c.execute("""CREATE TABLE IF NOT EXISTS creds (
                firstname TEXT,
                lastname TEXT,
                email TEXT UNIQUE,
                password TEXT,
                repassword TEXT
            )""")
            
            # Inserting data into the creds table 
            c.execute("INSERT INTO creds (firstname, lastname, email, password, repassword) VALUES (?, ?, ?, ?, ?)",
                      (firstname, lastname, email, password, repassword))
            conn.commit()
            conn.close()

            # Show a success message to the user
            messagebox.showinfo("Success", "Registration Successful")
            open_login()  # Go back to login frame

    frame = ctk.CTkFrame(parent, width=400, height=350, fg_color='white', border_color='black', border_width=2)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    frame.pack_propagate(False)

    title_label = ctk.CTkLabel(frame, text="Census 2025", font=ctk.CTkFont(size=36, weight="bold"))
    title_label.grid(column=0, row=0, sticky='w', padx=20, pady=20)

    reg_label = ctk.CTkLabel(frame, text="Registration", font=ctk.CTkFont(size=25, weight="bold"))
    reg_label.grid(column=0, row=1, sticky='w', padx=20, pady=20)

    firstname_label = ctk.CTkLabel(frame, text="First Name:")
    firstname_label.grid(column=0, row=2, sticky='w', padx=20, pady=20)
    firstname_entry = ctk.CTkEntry(frame)
    firstname_entry.grid(column=1, row=2, sticky='w', padx=20, pady=20)

    lastname_label = ctk.CTkLabel(frame, text="Last Name:")
    lastname_label.grid(column=0, row=3, sticky='w', padx=20, pady=20)
    lastname_entry = ctk.CTkEntry(frame)
    lastname_entry.grid(column=1, row=3, sticky='w', padx=20, pady=20)

    email_label = ctk.CTkLabel(frame, text="Email:")
    email_label.grid(column=0, row=4, sticky='w', padx=20, pady=20)
    email_entry = ctk.CTkEntry(frame)
    email_entry.grid(column=1, row=4, sticky='w', padx=20, pady=20)

    pass_label = ctk.CTkLabel(frame, text="Password:")
    pass_label.grid(column=0, row=5, sticky='w', padx=20, pady=20)
    pass_entry = ctk.CTkEntry(frame, show="*")
    pass_entry.grid(column=1, row=5, sticky='w', padx=20, pady=20)

    pass_confirm_label = ctk.CTkLabel(frame, text="Confirm Password:")
    pass_confirm_label.grid(column=0, row=6, sticky='w', padx=20, pady=20)
    pass_confirm_entry = ctk.CTkEntry(frame, show="*")
    pass_confirm_entry.grid(column=1, row=6, sticky='w', padx=20, pady=20)

    data_button = ctk.CTkButton(frame, text="Register", command=reg)
    data_button.grid(column=1, row=7, sticky='w', padx=20, pady=20)

    return frame
