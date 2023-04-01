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


    def run(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    calculator = BMI()
    calculator.run()