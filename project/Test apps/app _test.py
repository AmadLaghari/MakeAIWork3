import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from tkinter import *
import PIL.Image
import PIL.ImageTk
from PIL import ImageTk
from sklearn.utils import validation

# Model inladen
model = joblib.load("projects/my_model/Medische_data_model_Manual_scikitlearn2b.pkl")

lifespan = model.predict([[4, 3 , 4, 3, 4, 3]])[0]
print(lifespan)

# Tkinter window aanmaken
root = Tk()
root.geometry("600x700")
root.configure(bg='#F1CA9E')

# Logo inladen
photoimage = ImageTk.PhotoImage(file="C:/Users/amad_/makeaiwork3/projects/wassching.png")
root.iconphoto(True, photoimage)
root.title("Predicted Lifespan")

# Canvas aanmaken om foto weer te geven
canvas = Canvas(root,width=1, height=1)
canvas.create_image(2, 2, image=photoimage)
canvas.pack()

# invoervelden en labels aanmaken
input1_var = StringVar()
input2_var = StringVar()
input3_var = StringVar()
input4_var = StringVar()
input5_var = StringVar()
input6_var = StringVar()
input1_label = Label(root, text="Genetische leeftijd", font=("Helvetica", 16,), bg='#F1CA9E')
input1_entry = Scale(root, from_=0, to=150, orient=HORIZONTAL, variable=input1_var, bg='#F1CA9E')
input2_label = Label(root, text="BMI", font=("Helvetica", 16), bg='#F1CA9E')
input2_entry = Scale(root, from_=0, to=50, orient=HORIZONTAL, variable=input2_var, bg='#F1CA9E')
input3_label = Label(root, text="Sporten (Uren per week)", font=("Helvetica", 16), bg='#F1CA9E')
input3_entry = Scale(root, from_=0, to=24, orient=HORIZONTAL, variable=input3_var, bg='#F1CA9E')
input4_label = Label(root, text="Roken (Aantal sigaretten per dag)", font=("Helvetica", 16), bg='#F1CA9E')
input4_entry = Scale(root, from_=0, to=50, orient=HORIZONTAL, variable=input4_var, bg='#F1CA9E')
input5_label = Label(root, text="Alcohol (Aantal glazen per week)", font=("Helvetica", 16), bg='#F1CA9E')
input5_entry = Scale(root, from_=0, to=50, orient=HORIZONTAL, variable=input5_var, bg='#F1CA9E')
input6_label = Label(root, text="Suiker (per dag)", font=("Helvetica", 16), bg='#F1CA9E')
input6_entry = Scale(root, from_=0, to=50, orient=HORIZONTAL, variable=input6_var, bg='#F1CA9E')

# Submit knopje aanmaken
submit_button = Button(root, text="Submit", command=lambda: predict_lifespan())

# Output label aanmaken
output_label = Label(root, text="", font=("Helvetica", 16), bg='#F1CA9E')

# Functie om levensverwachting te voorspellen
def predict_lifespan():
    genetic = int(input1_var.get())
    BMI = int(input2_var.get())
    exercise = int(input3_var.get())
    smoking = int(input4_var.get())
    alcohol = int(input5_var.get())
    sugar = int(input6_var.get())

    lifespan = model.predict([[genetic, BMI , exercise, smoking, alcohol, sugar]])[0]
    output_label.configure(text=f"De verwachtte leeftijd van de patient is {int(lifespan)} jaar \n Premiefactor is {round(genetic/lifespan,2)}")

# invoervelden, labels en knop toevoegen aan TIinter window
input1_label.pack()
input1_entry.pack()
input2_label.pack()
input2_entry.pack()
input3_label.pack()
input3_entry.pack()
input4_label.pack()
input4_entry.pack()
input5_label.pack()
input5_entry.pack()
input6_label.pack()
input6_entry.pack()
submit_button.pack()
output_label.pack()

# Functie aanroepen
root.mainloop()

