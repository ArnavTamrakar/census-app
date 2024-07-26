import tkinter as tk
import customtkinter as ctk

def create_visuals_frame(parent, open_age_earning_scatter, open_homepage, open_earning_histogram, open_age_histogram, open_education_earning_boxplot, open_gender_piechart):

    frame = ctk.CTkFrame(parent, width=800, height=500, fg_color='white', border_color='black', border_width=2)
    frame.place(relx=.5, rely=.5, anchor='center')
    frame.pack_propagate(False)

    title_label = ctk.CTkLabel(frame, text="Select Visualization", font=ctk.CTkFont(size=36, weight="bold"))
    title_label.place(x=20, y=20)

    # button that navigates to age and earning scatter plot
    ageearning_scatter_button = ctk.CTkButton(frame,text = "Age and Earning Scatter Plot", font=ctk.CTkFont(size=20))
    ageearning_scatter_button.place(x=20, y=100)
    ageearning_scatter_button.bind("<Button-1>", lambda e: open_age_earning_scatter())

    # Button that navigates to earning distribution histogram
    earning_histogram_button = ctk.CTkButton(frame,text = "Earning Distribution Histogram", font=ctk.CTkFont(size=20))
    earning_histogram_button.place(x=400, y=100)
    earning_histogram_button.bind("<Button-1>", lambda e: open_earning_histogram())

    # Button that navigates to age distribution histogram
    age_histogram_button = ctk.CTkButton(frame,text = "Age Distrubution Histogram", font=ctk.CTkFont(size=20))
    age_histogram_button.place(x=20, y=200)
    age_histogram_button.bind("<Button-1>", lambda e: open_age_histogram())

    # Button that navigates to education and earning box plot
    education_earning_boxplot_button = ctk.CTkButton(frame,text = "Education and Earning Box Plot", font=ctk.CTkFont(size=20))
    education_earning_boxplot_button.place(x=400, y=200)
    education_earning_boxplot_button.bind("<Button-1>", lambda e: open_education_earning_boxplot())

    # Button that navigates to gender distribution pie chart
    gender_piechart_button = ctk.CTkButton(frame,text = "Gender Distribution Pie Chart", font=ctk.CTkFont(size=20))
    gender_piechart_button.place(x=20, y=300)
    gender_piechart_button.bind("<Button-1>", lambda e: open_gender_piechart())

    # back button to go back to homepage 
    back_label = ctk.CTkLabel(frame, cursor="hand2", text="< Back", text_color="blue")
    back_label.place(x=750, y=20)
    back_label.bind("<Button-1>",lambda e: open_homepage())

    return frame