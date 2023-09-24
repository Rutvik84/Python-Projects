from tkinter import *
from PIL import ImageTk, Image


raj = Tk()
raj.title("Virutal Quiz Arena")
raj.minsize(width=1200, height=675)

def menupage():
    raj.destroy()
    import Main

path="basic.jpg"


img = ImageTk.PhotoImage(Image.open(path))

label = Label(raj, text="Welcome",image=img)
label.pack(fill="both", expand="yes")


my_label1 = Label(text=("Virtual Quiz Arena"), font=("ObelixPro", 50), fg="Black")
my_label1.place(x=190, y=40)

btn_img = PhotoImage(file="button.png")
button = Button(image=btn_img, command=menupage)
button.place(x=480, y=540)

raj.mainloop()


