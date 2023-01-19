from tkinter import *
from tkinter import ttk
import joblib


class App:
    def __init__(self, master):
        self.master = master

        self.input1 = None
        self.create_grid()

        self.bmi()
   
    def create_grid(self):
        self.main_grid = ttk.Frame(self.master)
        self.main_grid.grid(column=0, row=0, sticky=(N, S, W, E))



        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
           

           
        self.right_column = ttk.Frame(self.main_grid, width=500)
        self.right_column.grid(column=2, row=1, sticky=(N, S, W, E))
           

    def bmi(self):
        for i in self.right_column.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.right_column, width=100, height=100)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='BMI')
        self.reg_txt.pack()
        self.input_entry = ttk.Entry(self.frame1)
        self.input_entry.pack()
        self.register_btn = ttk.Button(self.frame1, text="Next", command=self.genetic_age)
        self.register_btn.pack()

    def genetic_age(self):
        self.input1 = self.input_entry.get()
        for i in self.right_column.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.right_column, width=100, height=100)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='Genetic Age')
        self.reg_txt2.pack()
        self.input_entry2 = ttk.Entry(self.frame2)
        self.input_entry2.pack()
        self.genetic_age_btn = ttk.Button(self.frame2, text="Back", command=self.bmi)
        self.genetic_age_btn.pack()
        self.register_btn2 = ttk.Button(self.frame2, text="Next", command=self.sport)
        self.register_btn2.pack()


    def sport(self):
        self.input2 = self.input_entry2.get()
        for i in self.right_column.winfo_children():
            i.destroy()
        self.frame3 = Frame(self.right_column, width=100, height=100)
        self.frame3.pack()
        self.reg_txt3 = ttk.Label(self.frame3, text='Sport')
        self.reg_txt3.pack()
        self.slider = ttk.Scale(self.frame3, from_=0, to=10, orient="horizontal", command=self.set_slider_value)
        self.slider.pack()
        self.value = StringVar()
        self.value.set(0)
        self.value_label = ttk.Label(self.frame3, textvariable=self.value)
        self.value_label.pack()
        self.genetic_age_btn = ttk.Button(self.frame3, text="Back", command=self.genetic_age)
        self.genetic_age_btn.pack()
        self.register_btn3 = ttk.Button(self.frame3, text="Next", command=self.smoking)
        self.register_btn3.pack()

    def set_slider_value(self, value):
        value = int(float(value))
        if value > 10:
            value = 10
        elif value < 1:
            value = 1
        self.value.set(value)


       
    def smoking(self):
        self.input3 = self.slider.get()
        for i in self.right_column.winfo_children():
            i.destroy()
        self.frame4 = Frame(self.right_column, width=100, height=100)
        self.frame4.pack()
        self.reg_txt4 = ttk.Label(self.frame4, text='Smoking')
        self.reg_txt4.pack()
        self.slider4 = ttk.Scale(self.frame4, from_=0, to=10, orient="horizontal", command=self.set_slider_value4)
        self.slider4.pack()
        self.value4 = StringVar()
        self.value4.set(0)
        self.value_label4 = ttk.Label(self.frame4, textvariable=self.value4)
        self.value_label4.pack()
        self.smoking_btn = ttk.Button(self.frame4, text="Back", command=self.sport)
        self.smoking_btn.pack()
        self.register_btn4 = ttk.Button(self.frame4, text="Next", command=self.alcohol)
        self.register_btn4.pack()

    def set_slider_value4(self, value4):
        value4 = int(float(value4))
        if value4 > 10:
            value4 = 10
        elif value4 < 1:
            value4 = 1
        self.value4.set(value4)


    def alcohol(self):
        self.input4 = self.slider4.get()
        for i in self.right_column.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.right_column, width=100, height=100)
        self.frame5.pack()
        self.reg_txt5 = ttk.Label(self.frame5, text='Alcohol')
        self.reg_txt5.pack()
        self.slider5 = ttk.Scale(self.frame5, from_=0, to=10, orient="horizontal", command=self.set_slider_value5)
        self.slider5.pack()
        self.value5 = StringVar()
        self.value5.set(0)
        self.value_label5 = ttk.Label(self.frame5, textvariable=self.value5)
        self.value_label5.pack()
        self.alcohol_btn = ttk.Button(self.frame5, text="Back", command=self.smoking)
        self.alcohol_btn.pack()
        self.register_btn5 = ttk.Button(self.frame5, text="Predict", command=self.calculate)
        self.register_btn5.pack()

    def set_slider_value5(self, value5):
        value5 = int(float(value5))
        if value5 > 10:
            value5 = 10
        elif value5 < 1:
            value5 = 1
        self.value5.set(value5)


       
    def calculate(self):
        self.input5 = self.slider5.get()
        self.result = float(self.input1) + float(self.input2) + float(self.input3) + float(self.input4) + float(self.input5)
        for i in self.right_column.winfo_children():
            i.destroy()
        self.frame6 = Frame(self.right_column, width=100, height=100)
        self.frame6.pack()
        self.result_txt = ttk.Label(self.frame6, text='Result: {}'.format(self.result))
        self.result_txt.pack()




root = Tk()
app = App(root)
root.mainloop()
