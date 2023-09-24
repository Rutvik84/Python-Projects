import tkinter
from PIL import ImageTk, Image

menus = tkinter.Tk()
menus.title("Game Selection")
menus.minsize(width=500, height=300)

path = "bg.jpg"

img = ImageTk.PhotoImage(Image.open(path))

label = tkinter.Label(menus, image=img)
label.pack(fill="both", expand="yes")

# label
my_label1 = tkinter.Label(text="Choose Game", font=("Engravers MT", 50,), fg="Black")
my_label1.place(x=330, y=60)


def SnakeG():
    menus.destroy()
    import Basic

def FlappyB():
    menus.destroy()
    import flappyBird

def Pingpong():
    menus.destroy()
    import Start

# button
btn_img = ImageTk.PhotoImage(file="snake.jpg")
button = tkinter.Button(menus, image=btn_img,command=SnakeG)
button.place(x=450, y=400)
my_label3 = tkinter.Label(text="SNAKE GAME", font=("Comic Sans MS", 25,), fg="black")
my_label3.place(x=490, y=580)


#button2.
btn_vm = ImageTk.PhotoImage(file="flappybi.png",)
button = tkinter.Button(menus, image=btn_vm, command=FlappyB)
button.place(x=60, y=240)
my_label2 = tkinter.Label(text="Flappy Bird", font=("Comic Sans MS", 25,), fg="black")
my_label2.place(x=114, y=412)

#button3
btn_ss = ImageTk.PhotoImage(file="xyz.jpg",)
button = tkinter.Button(menus, image=btn_ss, command=Pingpong)
button.place(x=900, y=230)
my_label4 = tkinter.Label(text="Ping Pong", font=("Comic Sans MS", 25,), fg="black")
my_label4.place(x=970, y=430)


menus.mainloop()
