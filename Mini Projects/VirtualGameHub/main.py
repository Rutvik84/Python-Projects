from tkinter import *
from PIL import ImageTk, Image


raj = Tk()
raj.title("VirtualGameHUB")
raj.minsize(width=500, height=300)

def menupage():
    raj.destroy()
    import Menu

path="bg.jpg"

img = ImageTk.PhotoImage(Image.open(path))

label = Label(raj, text="Welcome",image=img)
label.pack(fill="both", expand="yes")


my_label1 = Label(text="Virtual Gaming Hub", font=("Engravers MT", 45), fg="Black")
my_label1.place(x=120, y=100)

btn_img = PhotoImage(file="button1.png")
button = Button(image=btn_img, command=menupage)
button.place(x=480, y=550)

raj.mainloop()


