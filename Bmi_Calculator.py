from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class BMI:
    def __init__(self):
        self.root = Tk()
        self.root.title("BMI calculator")
        self.root.geometry("470x580+300+200")
        self.root.resizable(0,0)
        self.root.configure(bg = "#f0f1f5")

        self.current_value = tk.DoubleVar()
        self.current_value_02 = tk.DoubleVar()

        self.label_01 = Label(self.root, font = "arial 60 bold", bg = "lightblue", fg = "#fff")
        self.label_01.place(x = 125, y = 305)

        self.label_02 = Label(self.root, font = "arial 20 bold", bg = "lightblue", fg = "#3b3a3a")
        self.label_02.place(x = 250, y = 430)

        self.label_03 = Label(self.root, font = "arial 10 ", bg = "lightblue")
        self.label_03.place(x = 200, y = 500)

    def entry_box(self):
        self.Height = StringVar()
        self.Weight = StringVar()
        self.height = Entry(self.root, textvariable = self.Height, width = 5,
                        font = 'arial 50', bg = "#fff", fg = "#000", bd = 0, justify = CENTER )
        self.height.place(x = 35, y = 160)
        self.Height.set(self.get_current_value())

        self.weight = Entry(self.root, textvariable = self.Weight, width = 5,
                         font = 'arial 50', bg = "#fff", fg = "#000", bd = 0, justify = CENTER)
        self.weight.place(x = 255, y = 160)
        self.Weight.set(self.get_current_value_02())      

    def get_current_value(self):
        return '{: .2f}'.format(self.current_value.get())
    
    def get_current_value_02(self):
        return '{: .2f}'.format(self.current_value_02.get())


    def BMI(self):
        self.h = float(self.Height.get())
        self.w = float(self.Weight.get())

        #convert height into meter
        self.m = self.h/100
        self.bmi = round(float(self.w/self.m**2), 1)
        self.label_01.config(text = self.bmi)

        if self.bmi <= 18.5:
            self.label_02.config(text = "Underweight!")
            self.label_03.config(text = "You have lower weight then normal body!")

        elif self.bmi > 18.5 and self.bmi <= 25:
            self.label_02.config(text = "Normal!")
            self.label_03.config(text = "It indicates that you are healthy!")
            
        elif self.bmi > 25 and self.bmi <= 30:
            self.label_02.config(text = "Overweight!")
            self.label_03.config(text = "It indicates that a person is \n slightly overweight! \n A doctor may advise to lose some \n weight for health reasons ")
            
        else:
            self.label_02.config(text = "Obes!")
            self.label_03.config(text = "Health may be at risk, if they do not \n lose your weight ! ")


    def run(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    calculator = BMI()
    calculator.run()