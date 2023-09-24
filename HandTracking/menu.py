import tkinter
from PIL import ImageTk, Image

menus = tkinter.Tk()
menus.title("Task Selection")
menus.minsize(width=500, height=300)

path = "what-is-computer-vision.jpg"

img = ImageTk.PhotoImage(Image.open(path))

label = tkinter.Label(menus, image=img)
label.pack(fill="both", expand="yes")

# label
my_label1 = tkinter.Label(text="Select Task ", font=("Times", 50, "bold"), fg="blue")
my_label1.place(x=450, y=100)


def virtualVC():
    menus.destroy()
    import VolumeHandControlAdvance

def VirtualVM():
    menus.destroy()
    import AIVirtualMouseProject


# button
btn_img = ImageTk.PhotoImage(file="finalvvc.jpg")
button = tkinter.Button(menus, image=btn_img, command=virtualVC)
button.place(x=300, y=250)

# button2
btn_vm = ImageTk.PhotoImage(file="finalVM.jpg")
button = tkinter.Button(menus, image=btn_vm, command=VirtualVM)
button.place(x=700, y=250)

menus.mainloop()










