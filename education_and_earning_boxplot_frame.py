import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd

def create_education_earning_frame(parent, open_visuals):
    # connecting to database
    conn = sqlite3.connect("census.db")
    # querying the database
    query = '''
    SELECT Education, AnnualEarning
    FROM census_data
    ''' 
    # load data into dataframe
    data = pd.read_sql_query(query,conn)

    conn.close()

    # extracting data
    earning = data["AnnualEarning"]
    education=data["Education"]

    # plot the boxplot
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    data.boxplot(column="AnnualEarning", by="Education", ax=ax)
    ax.set_title('Earnings Distribution by Education Level')
    ax.set_xlabel('Education')
    ax.set_ylabel('Annual Earnings')
    plt.suptitle('')


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