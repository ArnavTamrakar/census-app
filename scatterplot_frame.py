import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_ageearning_scatter_frame(parent, open_visuals):
    # Connect to SQLite database
    conn = sqlite3.connect('census.db')  
    # Define your query to select Age and AnnualEarning
    query = '''
    SELECT Age, AnnualEarning
    FROM census_data
    '''

    # Load data into a DataFrame
    data = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Extract Age and AnnualEarning columns
    ages = data['Age']
    earnings = data['AnnualEarning']

    # Create a scatter plot
    fig1, ax1 = plt.subplots(figsize=(5, 4), dpi=100)
    ax1.scatter(ages, earnings, color='black', alpha=0.7)

    # Add title and labels
    ax1.set_title('Scatter Plot of Age vs Annual Earnings')
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Annual Earning')

    frame =tk.Frame(parent, width=1120, height=750, background='white')
    frame.place(anchor='center', relx=.5, rely=.5)
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

