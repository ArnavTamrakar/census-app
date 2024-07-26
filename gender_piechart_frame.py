import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import sqlite3

def create_genderdistribution_frame(parent, open_visuals):
    conn=sqlite3.connect("census.db")

    query ='''
    SELECT Sex
    FROM census_data
    '''

    df=pd.read_sql_query(query,conn)

    conn.close()

    df['gender'] = df['Sex'].map({1: 'Male', 2: 'Female'})

    gender_counts = df['gender'].value_counts()

    # Extract data
    labels = gender_counts.index
    sizes = gender_counts.values

    # Plot
    fig, ax = plt.subplots(figsize=(5,4), dpi=100)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Gender Distribution")

    frame =tk.Frame(parent, width=1120, height=750, background='white')
    frame.place(anchor='center', relx=.5, rely=.5)
    frame.pack_propagate(False)


    # Create a FigureCanvasTkAgg object to render the Matplotlib figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    # Render the figure on the canvas
    canvas.draw()
    # Add the canvas widget to the frame, making it fill the available space
    canvas.get_tk_widget().pack(side='left', fill='both', expand = True)


    back_label = tk.Label(frame, text="< Back", fg="blue", cursor="hand2" )
    back_label.pack(pady=20)
    back_label.bind("<Button-1>", lambda e:open_visuals())

    return frame
    