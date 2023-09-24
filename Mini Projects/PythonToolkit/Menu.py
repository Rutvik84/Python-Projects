import tkinter
from PIL import ImageTk, Image

menus = tkinter.Tk()
menus.title("Choose Application")
menus.minsize(width=500, height=300)

path = "finalbg.jpg"

img = ImageTk.PhotoImage(Image.open(path))

label = tkinter.Label(menus, image=img)
label.pack(fill="both", expand="yes")

# label
my_label1 = tkinter.Label(text="Choose Application", font=("ObelixPro", 50,), fg="Black")
my_label1.place(x=200, y=60)


def MusicP():
    menus.destroy()
    import player

def DailyEx():
    menus.destroy()
    import DailyExpenses

def WeatherApp():
    menus.destroy()
    import application

def Menu2():
    menus.destroy()
    import Menu2

# button1
btn_img = ImageTk.PhotoImage(file="musifin.jpg")
button = tkinter.Button(menus, image=btn_img,command=MusicP)
button.place(x=450, y=400)
my_label3 = tkinter.Label(text="Music Player", font=("Comic Sans MS", 25,), fg="black")
my_label3.place(x=490, y=590)


#button2.
btn_vm = ImageTk.PhotoImage(file="daily.jpg",)
button = tkinter.Button(menus, image=btn_vm, command=DailyEx)
button.place(x=60, y=230)
my_label2 = tkinter.Label(text="Daily Expenses", font=("Comic Sans MS", 25,), fg="black")
my_label2.place(x=81, y=422)


btn_ss = ImageTk.PhotoImage(file="images.jpg",)
button = tkinter.Button(menus, image=btn_ss,width=260, command=WeatherApp)
button.place(x=850, y=230)
my_label4 = tkinter.Label(text="Weather App", font=("Comic Sans MS", 25,), fg="black")
my_label4.place(x=875, y=420)


btn_rs = ImageTk.PhotoImage(file="next.png",)
button = tkinter.Button(menus, image=btn_rs,width=100,height=51 ,command=Menu2)
button.place(x=1080, y=600)





menus.mainloop()
