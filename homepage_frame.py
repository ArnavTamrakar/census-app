import customtkinter as ctk
import tkinter
from tkinter import messagebox
import sqlite3

def create_homepage_frame(parent, open_login, open_details, open_visuals):
    frame = ctk.CTkFrame(parent, width=450, height=350, fg_color='white', border_color='black', border_width=2)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    frame.pack_propagate(False)

    title_label = ctk.CTkLabel(frame, text="Welcome to Census 2025", font=ctk.CTkFont(size=36, weight="bold"))
    title_label.pack(pady=(20, 40))

    # Button to go to details frame
    data_button = ctk.CTkButton(frame, text="Enter Details", font=ctk.CTkFont(size=20))
    data_button.pack(pady=(0, 20))
    data_button.bind("<Button-1>", lambda e: open_details())

    # Button to go to visualization frame
    visuals_button = ctk.CTkButton(frame, text="Visualizations", font=ctk.CTkFont(size=20))
    visuals_button.pack(pady=(0, 20))
    visuals_button.bind("<Button-1>", lambda e: open_visuals())

    return frame
