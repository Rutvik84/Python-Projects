from tkinter import *
from PIL import ImageTk, Image


raj = Tk()
raj.title("Python All in OnePlace")
raj.minsize(width=1200, height=675)

def menupage():
    raj.destroy()
    import Menu

path="finalbg.jpg"


img = ImageTk.PhotoImage(Image.open(path))

label = Label(raj, text="Welcome",image=img)
label.pack(fill="both", expand="yes")


my_label1 = Label(text=("Python All in OnePlace"), font=("ObelixPro", 30), fg="Black")
my_label1.place(x=274, y=100)

btn_img = PhotoImage(file="button.png")
button = Button(image=btn_img, command=menupage)
button.place(x=480, y=450)

raj.mainloop()


