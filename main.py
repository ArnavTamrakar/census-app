import customtkinter as ctk
from login_frame import create_login_frame
from register_frame import create_register_frame
from homepage_frame import create_homepage_frame
from details_frame import create_details_frame
from scatterplot_frame import create_ageearning_scatter_frame
from visuals_frame import create_visuals_frame
from histogram_earning_frame import create_earning_histogram_frame
from histogram_age_frame import create_age_histogram_frame
from education_and_earning_boxplot_frame import create_education_earning_frame
from gender_piechart_frame import create_genderdistribution_frame

def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Census 2025")
    root.geometry("900x600")

    frames = {}

    # Define the show_frame function that will be used for frame transitions
    def show_frame(frame_name):
        for name, frame in frames.items():
            frame.place_forget()  # Hide all frames
        frames[frame_name].place(relx=0.5, rely=0.5, anchor='center')  # Show the requested frame

    # Initialize frames after defining show_frame
    frames["Login"] = create_login_frame(root, lambda: show_frame("Register"), lambda: show_frame("Homepage"))
    frames["Register"] = create_register_frame(root, lambda: show_frame("Login"))
    frames["Homepage"] = create_homepage_frame(root, lambda: show_frame("Login"), lambda: show_frame("Details"), lambda: show_frame("Visuals"))
    frames["Details"] = create_details_frame(root, lambda: show_frame("Homepage"))
    frames["Visuals"] = create_visuals_frame(root, lambda: show_frame("Scatter"), lambda: show_frame("Homepage"), lambda: show_frame("EarningHistogram"), 
                                             lambda: show_frame("AgeHistogram"), lambda: show_frame("EducationEarningBoxplot"), lambda: show_frame("GenderPiechart"))
    frames["Scatter"] = create_ageearning_scatter_frame(root, lambda: show_frame("Visuals"))
    frames["EarningHistogram"] = create_earning_histogram_frame(root, lambda: show_frame("Visuals"))
    frames["AgeHistogram"] = create_age_histogram_frame(root, lambda: show_frame("Visuals"))
    frames["EducationEarningBoxplot"] = create_education_earning_frame(root, lambda: show_frame("Visuals"))
    frames["GenderPiechart"] = create_genderdistribution_frame(root, lambda: show_frame("Visuals"))
    
    # Display the login frame initially
    show_frame("Login")

    root.mainloop()

if __name__ == "__main__":
    main()
