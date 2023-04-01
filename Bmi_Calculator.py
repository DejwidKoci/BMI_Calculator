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


        self.picture()
        self.get_current_value()
        self.change_style_01()
        self.get_current_value_02()
        self.change_style_02()
        
        self.entry_box()

        Button(self.root, text = "View report", width = 15, height = 2,
               font = "arial 10 bold", bg = "#1f6e68", fg = "white", 
               command = self.BMI).place(x = 280, y = 340)
        
        self.label_01 = Label(self.root, font = "arial 60 bold", bg = "lightblue", fg = "#fff")
        self.label_01.place(x = 125, y = 305)

        self.label_02 = Label(self.root, font = "arial 20 bold", bg = "lightblue", fg = "#3b3a3a")
        self.label_02.place(x = 250, y = 430)

        self.label_03 = Label(self.root, font = "arial 10 ", bg = "lightblue")
        self.label_03.place(x = 200, y = 500)
        
        
        
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

    

    def picture(self):
        
        #icon
        self.image_icon = PhotoImage(file = "images/icon.png")
        self.root.iconphoto(False, self.image_icon)

        #top
        self.top = PhotoImage(file = "images/top.png")
        self.top_image = Label(self.root, image = self.top, background = "#f0f1f5")
        self.top_image.place(x = -10, y = -10)

        #bottom box
        Label(self.root, width = 72, height = 18, bg = "lightblue").pack(side = BOTTOM)

        #two boxes
        self.box = PhotoImage(file = "Images/box.png")
        Label(self.root,image = self.box).place(x = 20, y = 100)
        Label(self.root, image = self.box).place(x = 240, y = 100)

        #scale
        self.scale = PhotoImage(file = "images/scale.png")
        Label(self.root, image = self.scale, bg = "lightblue").place(x = 20, y = 310)

        #man icone
        self.secondimage = Label(self.root, bg = "lightblue")
        self.secondimage.place(x = 70, y = 530)
     

    def entry_box(self):
        self.Height = StringVar()
        self.Weight = StringVar()
        self.text_h = Label(self.root, text = "Height (cm)", width = 10, font = 'arial 15',
                            bg = "#fff", fg = "#000", bd = 0, justify = CENTER)
        self.text_h.place(x = 80, y = 120)
        self.height = Entry(self.root, textvariable = self.Height, width = 5,
                        font = 'arial 50', bg = "#fff", fg = "#000", bd = 0, justify = CENTER )
        self.height.place(x = 35, y = 160)
        self.Height.set(self.get_current_value())

        self.text_w = Label(self.root, text = "Weight (kg)", width = 10, font = 'arial 15',
                            bg = "#fff", fg = "#000", bd = 0, justify = CENTER)
        self.text_w.place(x = 300, y = 120)
        self.weight = Entry(self.root, textvariable = self.Weight, width = 5,
                         font = 'arial 50', bg = "#fff", fg = "#000", bd = 0, justify = CENTER)
        self.weight.place(x = 255, y = 160)
        self.Weight.set(self.get_current_value_02())      

        

    def get_current_value(self):
        return '{: .2f}'.format(self.current_value.get())
    
    def slider_changed(self,event):
        self.Height.set(self.get_current_value())
    
        self.size = int(float(self.get_current_value()))
        self.img = (Image.open("images/man.png"))
        resized_image = self.img.resize((50, 10 + self.size))
        photo2 = ImageTk.PhotoImage(resized_image)
        self.secondimage.config(image = photo2)
        self.secondimage.place(x = 70, y = 550 - self.size)
        self.secondimage.image = photo2 

    def change_style_01(self):
        self.style = ttk.Style()
        self.style.configure("TScale", background = "white")
        slider = ttk.Scale(self.root, from_ = 0, to = 220, orient = 'horizontal',
                            style = "TScale", command = self.slider_changed, 
                            variable = self.current_value)
        slider.place(x = 80, y = 250)
    

    def get_current_value_02(self):
        return '{: .2f}'.format(self.current_value_02.get())
    
    def slider_changed_02(self,event):
        self.Weight.set(self.get_current_value_02())

    def change_style_02(self):
        self.style_02 = ttk.Style()
        self.style_02.configure("TScale", background = "white")
        slider_02 = ttk.Scale(self.root, from_ = 0, to = 220, orient = 'horizontal',
                            style = "TScale", command = self.slider_changed_02, 
                            variable = self.current_value_02)
        slider_02.place(x = 300, y = 250)


   
    def run(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    calculator = BMI()
    calculator.run()