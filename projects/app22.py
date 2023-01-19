import tkinter
import joblib
from tkinter import Scale
from tkinter import StringVar
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from tkinter import *
import PIL.Image
import PIL.ImageTk
from PIL import ImageTk
from sklearn.utils import validation
import jinja2
import pdfkit
from datetime import datetime

import tkinter.messagebox
import customtkinter
from tkinter import PhotoImage
from PIL import Image
from tkinter import StringVar
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

model = joblib.load("C:/Users/amad_/makeaiwork3/projects/my_model/Medische_data_model_Manual_scikitlearn2b.pkl")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Lifometer")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.pages = []
        self.current_page = None
        self.create_input_1_page()
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        my_image = customtkinter.CTkImage(light_image=Image.open("C:/Users/amad_/makeaiwork3/projects/wassching.png"),
            dark_image=Image.open("C:/Users/amad_/makeaiwork3/projects/wassching.png"),
            size=(50,50),
            )
        self.button_logo = customtkinter.CTkButton(master=self, image=my_image, fg_color="#2b2b2c", text="", command=None)
        self.button_logo.grid(row=0, column=0, columnspan=1, padx=20, pady=100, sticky="nesw")
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame)


        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Documentatie", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=0, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Update", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="", anchor="w")
        self.scaling_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 20))


        self.main_button_1 = customtkinter.CTkButton(master=self, text ="Advies", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text ="Exit", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=2, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


        self.bmi = customtkinter.CTkFrame(self, width=250)
        self.length_label = customtkinter.CTkLabel(self.bmi, text="BMI Calculator")
        self.length_label.grid(row=0, column=0, padx=20, pady=10)
        self.bmi.grid(row=0, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.length_label = customtkinter.CTkLabel(self.bmi, text="Length (m)")
        self.length_label.grid(row=1, column=0, padx=20, pady=10)
        self.input_length_entry = customtkinter.CTkEntry(self.bmi, placeholder_text='Length (m)')
        self.input_length_entry.grid(row=2, column=0, padx=00, pady=5)

        self.weight_label = customtkinter.CTkLabel(self.bmi, text="Weight (kg)")
        self.weight_label.grid(row=3, column=0, padx=20, pady=10)
        self.input_weight_entry = customtkinter.CTkEntry(self.bmi, placeholder_text='Weight (kg)')
        self.input_weight_entry.grid(row=4, column=0, padx=00, pady=5)

        self.input_bmi_button = customtkinter.CTkButton(self.bmi, text="Calculate", command=self.calculate_bmi)
        self.input_bmi_button.grid(row=5, column=0, padx=20, pady=10)
        self.output_entry = customtkinter.CTkLabel(self.bmi, text="")
        self.output_entry.grid(row=6, column=0, padx=20, pady=10)
       
    def calculate_bmi(self):
        try:
            length = float(self.input_length_entry.get())
            weight = float(self.input_weight_entry.get())
            bmi = weight / (length*length)
            self.output_entry.configure(text=f"BMI: {int(bmi):.0f}")
        except ValueError:
            tkinter.messagebox.showerror("Invalid input", "Please enter a valid number for length and weight.")



    def create_input_1_page(self):
        self.input_1_frame = customtkinter.CTkFrame(self)
        self.input_1_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=20, pady=10)
        self.input_1_label = customtkinter.CTkLabel(self.input_1_frame, text="Genetic Age")
        self.input_1_label.grid(row=1, column=1, padx=20, pady=10)
        self.input_1_entry = customtkinter.CTkEntry(self.input_1_frame)
        self.input_1_entry.grid(row=2, column=1, padx=20, pady=10)
        def validate_and_next():
            input_value = self.input_1_entry.get()
            try:
                value = int(input_value)
                if value >= 70 and value <= 122:
                    self.create_input_2_page()
                else:
                    show_error_message()
            except ValueError:
                show_error_message()

        def show_error_message():
            tkinter.messagebox.showerror("Invalid Input", "Please enter a number between 70 and 122.")

        self.input_1_next_button = customtkinter.CTkButton(self.input_1_frame, text="Next", command=validate_and_next)
        self.input_1_next_button.grid(row=2, column=2, padx=20, pady=10)
        self.current_page = self.input_1_frame



    def create_input_2_page(self):
        self.input_1_value = self.input_1_entry.get()

        if self.current_page is not None:
            self.current_page.grid_remove()
        self.input_2_frame = customtkinter.CTkFrame(self)
        self.input_2_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.input_2_label = customtkinter.CTkLabel(self.input_2_frame, text="BMI")
        self.input_2_label.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        self.input_2_entry = customtkinter.CTkEntry(self.input_2_frame)
        self.input_2_entry.grid(row=2, column=1, padx=20, pady=10)
        self.input_2_back_button = customtkinter.CTkButton(self.input_2_frame, text="Back", command=self.create_input_1_page)
        self.input_2_back_button.grid(row=2, column=0, padx=20, pady=10)
        def validate_and_next():
            input_value = self.input_2_entry.get()
            try:
                value = int(input_value)
                if value >= 13.5 and value <= 105.3:
                    self.create_input_3_page()
                else:
                    show_error_message()
            except ValueError:
                show_error_message()

        def show_error_message():
            tkinter.messagebox.showerror("Invalid Input", "Please enter a number between 13.5 and 105.3.")

        self.input_2_next_button = customtkinter.CTkButton(self.input_2_frame, text="Next", command=validate_and_next)
        self.input_2_next_button.grid(row=2, column=2, padx=20, pady=10)
        self.current_page = self.input_2_frame


       
    def create_input_3_page(self):
        self.input_2_value = self.input_2_entry.get()

        if self.current_page is not None:
            self.current_page.grid_remove()
        self.input_3_frame = customtkinter.CTkFrame(self)
        self.input_3_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.input_3_label = customtkinter.CTkLabel(self.input_3_frame, text="Sports")
        self.input_3_label.grid(row=0, column=1, padx=20, pady=10)
        self.input_3_slider = Scale(self.input_3_frame, from_=0, to=7, orient="horizontal")
        self.input_3_slider.set(0) # set the default value to 5
        self.input_3_slider.grid(row=2, column=1, padx=20, pady=10)
        self.input_3_back_button = customtkinter.CTkButton(self.input_3_frame, text="Back", command=self.create_input_2_page)
        self.input_3_back_button.grid(row=2, column=0, padx=20, pady=10)
        self.input_3_next_button = customtkinter.CTkButton(self.input_3_frame, text="Next", command=self.create_input_4_page)
        self.input_3_next_button.grid(row=2, column=2, padx=20, pady=10)
        self.current_page = self.input_3_frame

    def create_input_4_page(self):
        self.input_3_value = self.input_3_slider.get()

        if self.current_page is not None:
            self.current_page.grid_remove()
        self.input_4_frame = customtkinter.CTkFrame(self)
        self.input_4_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.input_4_label = customtkinter.CTkLabel(self.input_4_frame, text="Smoking")
        self.input_4_label.grid(row=0, column=1, padx=20, pady=10)
        self.input_4_slider = Scale(self.input_4_frame, from_=1, to=10, orient="horizontal")
        self.input_4_slider.set(5) # set the default value to 5
        self.input_4_slider.grid(row=2, column=1, padx=20, pady=10)
        self.input_4_back_button = customtkinter.CTkButton(self.input_4_frame, text="Back", command=self.create_input_3_page)
        self.input_4_back_button.grid(row=2, column=0, padx=20, pady=10)
        self.input_4_next_button = customtkinter.CTkButton(self.input_4_frame, text="Next", command=self.create_input_5_page)
        self.input_4_next_button.grid(row=2, column=2, padx=20, pady=10)
        self.current_page = self.input_4_frame


    def create_input_5_page(self):
        self.input_4_value = self.input_4_slider.get()

        if self.current_page is not None:
            self.current_page.grid_remove()
        self.input_5_frame = customtkinter.CTkFrame(self)
        self.input_5_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.input_5_label = customtkinter.CTkLabel(self.input_5_frame, text="Alcohol")
        self.input_5_label.grid(row=0, column=1, padx=20, pady=10)
        self.input_5_slider = Scale(self.input_5_frame, from_=1, to=10, orient="horizontal")
        self.input_5_slider.set(5) # set the default value to 5
        self.input_5_slider.grid(row=2, column=1, padx=20, pady=10)
        self.input_5_back_button = customtkinter.CTkButton(self.input_5_frame, text="Back", command=self.create_input_4_page)
        self.input_5_back_button.grid(row=2, column=0, padx=20, pady=10)
        self.input_5_next_button = customtkinter.CTkButton(self.input_5_frame, text="Next", command=self.create_input_6_page)
        self.input_5_next_button.grid(row=2, column=2, padx=20, pady=10)
        self.current_page = self.input_5_frame


    def create_input_6_page(self):
        self.input_5_value = self.input_5_slider.get()

        if self.current_page is not None:
            self.current_page.grid_remove()
        self.input_6_frame = customtkinter.CTkFrame(self)
        self.input_6_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.input_6_label = customtkinter.CTkLabel(self.input_6_frame, text="Sugar")
        self.input_6_label.grid(row=0, column=1, padx=20, pady=10)
        self.input_6_slider = Scale(self.input_6_frame, from_=1, to=10, orient="horizontal")
        self.input_6_slider.set(5) # set the default value to 5
        self.input_6_slider.grid(row=2, column=1, padx=20, pady=10)
        self.input_6_back_button = customtkinter.CTkButton(self.input_6_frame, text="Back", command=self.create_input_5_page)
        self.input_6_back_button.grid(row=2, column=0, padx=20, pady=10)
        self.input_6_next_button = customtkinter.CTkButton(self.input_6_frame, text="predict", command=self.create_output_page)
        self.input_6_next_button.grid(row=2, column=2, padx=20, pady=10)
        self.current_page = self.input_6_frame



    def create_output_page(self):
        self.input_6_value = self.input_6_slider.get()
        self.input_6_frame.destroy()

        self.output_frame = customtkinter.CTkFrame(self)
        self.output_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.output_label = customtkinter.CTkLabel(self.output_frame, text="Lifespan")
        self.output_label.grid(row=0, column=1, padx=20, pady=10)



        genetic = int(self.input_1_value)
        BMI = int(self.input_2_value)
        exercise = int(self.input_3_value)
        smoking = int(self.input_4_value)
        alcohol = int(self.input_5_value)
        sugar = int(self.input_6_value)

        self.output_value = int(model.predict([[genetic, BMI , exercise, smoking, alcohol, sugar]])[0])


        self.output_entry = customtkinter.CTkLabel(self.output_frame, text=self.output_value)
        self.output_entry.grid(row=2, column=1, padx=20, pady=10)
        self.output_start_over_button = customtkinter.CTkButton(self.output_frame, text="Start Again", command=self.create_start_over_page)
        self.output_start_over_button.grid(row=2, column=2, padx=20, pady=10)

    def create_start_over_page(self):
        self.output_frame.destroy()
        self.create_input_1_page()




        # set default values

        self.checkbox_2.configure(state="disabled")
        self.switch_2.configure(state="disabled")
        self.checkbox_1.select()
        self.switch_1.select()
        # self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        self.textbox.insert("0.0", "NOTES.....\n\n")
       



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
