from tkinter import *
from PIL import ImageTk, Image

raj = Tk()
raj.title("open Cv")
raj.minsize(width=500, height=300)


def menupage():
    raj.destroy()
    import menu



path="what-is-computer-vision.jpg"

img = ImageTk.PhotoImage(Image.open(path))

label = Label(raj, text="Welcome",image=img)
label.pack(fill="both", expand="yes")

# label
my_label1 = Label(text="Welcome to open CV ", font=("Times", 50, "bold"), fg="blue")
my_label1.place(x=360, y=100)

btn_img = PhotoImage(file="button.png")
button = Button(image=btn_img, command=menupage)
button.place(x=630, y=280)

raj.mainloop()


