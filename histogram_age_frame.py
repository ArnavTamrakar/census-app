import sqlite3
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def create_age_histogram_frame(parent, open_visuals):
    # Connect to SQLite database
    conn=sqlite3.connect("census.db")
    # Define you query to select age 
    query = '''
    SELECT Age
    FROM census_data
    '''
    # Load data into dataframe
    data = pd.read_sql_query(query, conn)
    # Close the database connection
    conn.close()

    # Extract required column
    age = data["Age"]

    # Create histogram 
    fig1, ax1=plt.subplots(figsize=(5,4), dpi=100)
    ax1.hist(age, density=True, color="blue")
    ax1.set_title("Distribution of Age")
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Percentage")

    frame =tk.Frame(parent, width=1120, height=750, background='white')
    frame.place(anchor='center')
    frame.pack_propagate(False)


    # Create a FigureCanvasTkAgg object to render the Matplotlib figure in Tkinter
    canvas = FigureCanvasTkAgg(fig1, master=frame)
    # Render the figure on the canvas
    canvas.draw()
    # Add the canvas widget to the frame, making it fill the available space
    canvas.get_tk_widget().pack(side='left', fill='both', expand = True)


    back_label = tk.Label(frame, text="< Back", fg="blue", cursor="hand2" )
    back_label.pack(pady=20)
    back_label.bind("<Button-1>", lambda e:open_visuals())

    return frame
