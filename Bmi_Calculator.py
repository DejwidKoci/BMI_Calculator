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
    
    def run(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    calculator = BMI()
    calculator.run()