import customtkinter as ctk
import tkinter
from tkinter import messagebox
from tkinter import END
import sqlite3



def create_details_frame(parent, open_homepage):
    # Function to display an error message using Tkinter's messagebox
    def show_warning():
        messagebox.showwarning(title="Error", message="All fields need to be filled", icon="warning")
    
    # Data entry function
    def enter_data():
        firstname = first_name_entry.get()
        middlename = middle_name_entry.get()
        lastname = last_name_entry.get()
        state = state_combobox.get()
        age = age_entry.get()
        annualearning = annual_earning_entry.get()
        sex = radio_var.get()
        maritalstatus = marital_status_combobox.get()
        education = education_combobox.get()
        
        # If statement to make sure that all the entry requirements are filled by the user
        if (firstname and lastname and state in states_option and 
            education in education_options and maritalstatus in marital_status_options):

            print(firstname, lastname, state, age, annualearning, sex, maritalstatus, education)
            
            # Create database
            conn = sqlite3.connect('census.db')
            cursor = conn.cursor()
            table_create_query = '''CREATE TABLE IF NOT EXISTS census_data (
                FirstName TEXT,
                MiddleName TEXT, 
                LastName TEXT,
                State TEXT,
                Age INT,
                AnnualEarning INT,
                Sex INT,
                MaritalStatus TEXT,
                Education TEXT
            )'''
            cursor.execute(table_create_query)
            
            # Insert data into census_data table
            cursor.execute("INSERT OR IGNORE INTO census_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                           (firstname, middlename, lastname, state, age, annualearning, sex, maritalstatus, education))
            
            
            # Commit the changes and close the database
            conn.commit()
            conn.close()
            # Success messagebox and clearing the entry for next use
            messagebox.showinfo(title="Success", message="Your data has been entered successfully")
            first_name_entry.delete(0, 'end')
            middle_name_entry.delete(0, 'end')
            last_name_entry.delete(0, 'end')
            state_combobox.set('')
            age_entry.delete(0, 'end')
            annual_earning_entry.delete(0, 'end')
            radio_var.set('')
            marital_status_combobox.set('')
            education_combobox.set('')
            

        # Else statement in case required data isn't filled
        else:
            show_warning()
            print("Wrong data entered by the user.")

    # Frame
    frame = ctk.CTkFrame(parent, width=1000, height=700, fg_color='white', border_color='black', border_width=2)
    frame.place(relx=0.5, rely=0.5, anchor='center')


    # Labels and entries for user information
    first_name_label = ctk.CTkLabel(frame, text="First Name")
    last_name_label = ctk.CTkLabel(frame, text="Last Name")
    middle_name_label = ctk.CTkLabel(frame, text="Middle Name")
    first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    last_name_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    middle_name_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    first_name_entry = ctk.CTkEntry(frame, placeholder_text="eg: Ben")
    middle_name_entry = ctk.CTkEntry(frame, placeholder_text="eg: Man")
    last_name_entry = ctk.CTkEntry(frame, placeholder_text="eg: Dover")
    first_name_entry.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    middle_name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    last_name_entry.grid(row=2, column=2, padx=10, pady=10)

    # Label and combobox for state selection
    state_label = ctk.CTkLabel(frame, text="State")
    state_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    states_option = ["SA", "WA", "NSW", "VIC", "QLD", "NT","TAS"]
    state_combobox = ctk.CTkComboBox(frame, values=states_option)
    state_combobox.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    state_combobox.set("eg: SA")  

    # Entry box and label for age
    age_label = ctk.CTkLabel(frame, text="Age")
    age_entry = ctk.CTkEntry(frame, placeholder_text="eg: 20")
    age_label.grid(row=3, column=1, sticky="w", padx=15)
    age_entry.grid(row=4, column=1)

    # Entry box and label for annual earning
    annual_earning_label = ctk.CTkLabel(frame, text="Annual Earning")
    annual_earning_entry = ctk.CTkEntry(frame, placeholder_text="eg: 100000")
    annual_earning_label.grid(row=3, column=2, sticky="w", padx=15)
    annual_earning_entry.grid(row=4, column=2)

    # Button to submit the data
    data_button = ctk.CTkButton(frame, text="Enter data", command=enter_data)
    data_button.grid(row=8, column=0, sticky="news", padx=20, pady=10)

    # Gender selection
    gender_label = ctk.CTkLabel(frame, text="Sex")
    radio_var = tkinter.IntVar(value=0)
    radiobutton_1 = ctk.CTkRadioButton(frame, text="Male", variable=radio_var, value=1)
    radiobutton_2 = ctk.CTkRadioButton(frame, text="Female", variable=radio_var, value=2)
    radiobutton_1.grid(row=6, column=0, sticky="news", padx=20, pady=10)
    radiobutton_2.grid(row=7, column=0, sticky="news", padx=20, pady=5)
    gender_label.grid(row=5, column=0, sticky="w", padx=20, pady=5)

    # Combo box for marital status selection
    marital_status_options = ["Unmarried", "Married", "Divorced"]
    marital_status_combobox = ctk.CTkComboBox(frame, values=marital_status_options)
    marital_status_combobox.grid(row=6, column=1, padx=10, pady=10, sticky="w")
    marital_status_combobox.set("eg: Married") 

    # Label for marital status selection
    marital_status_label = ctk.CTkLabel(frame, text="Marital Status")
    marital_status_label.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Combo box for education level
    education_options = [
        "Primary School",
        "Middle School",
        "High School",
        "Associate Degree",
        "Bachelor's Degree",
        "Master's Degree",
        "Doctorate (Ph.D.)",
        "Professional Certification",
        "Trade School",
        "Vocational Training",
        "Diploma",
        "Postgraduate Certificate",
        "Postgraduate Diploma"
    ]
    education_label = ctk.CTkLabel(frame, text="Education")
    education_label.grid(row=5, column=2, padx=20, pady=10, sticky="w")
    education_combobox = ctk.CTkComboBox(frame, values=education_options)
    education_combobox.grid(row=6, column=2, padx=20, pady=10, sticky="ew")
    education_combobox.set("eg: Diploma")

    # Back label to go back to homepage 
    goback_label = ctk.CTkLabel(frame,text = '< Back', text_color="blue" )
    goback_label.grid(row = 8, column = 3, padx = (0,20))
    goback_label.bind("<Button-1>", lambda e: open_homepage())

    return frame