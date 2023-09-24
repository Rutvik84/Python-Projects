import tkinter
from PIL import ImageTk, Image

menus = tkinter.Tk()
menus.title("Choose Game")
menus.minsize(width=500, height=300)

path = "finalbg.jpg"

img = ImageTk.PhotoImage(Image.open(path))

label = tkinter.Label(menus, image=img)
label.pack(fill="both", expand="yes")

# label
my_label1 = tkinter.Label(text="Choose Application", font=("ObelixPro", 50,), fg="Black")
my_label1.place(x=190, y=60)


def QrCode():
    menus.destroy()
    import qrCode

def CurrencyConv():
    menus.destroy()
    import currencyconverter

def back():
    menus.destroy()
    import Menu

#button3
btn_ww = ImageTk.PhotoImage(file="qr.jpg",)
button = tkinter.Button(menus, image=btn_ww, command=QrCode)
button.place(x=135, y=230)
my_label1 = tkinter.Label(text="Qr CodeScanner", font=("Comic Sans MS", 25,), fg="black")
my_label1.place(x=146, y=420)

#button
btn_ss = ImageTk.PhotoImage(file="currency.png",)
button = tkinter.Button(menus, image=btn_ss,width=300,height=168, command=CurrencyConv)
button.place(x=750, y=230)
my_label5 = tkinter.Label(text="Currency Converter", font=("Comic Sans MS", 25,), fg="black")
my_label5.place(x=750, y=406)

btn_aa = ImageTk.PhotoImage(file="back.png",)
button = tkinter.Button(menus, image=btn_aa,width=100,height=51 ,command=back)
button.place(x=40, y=600)

menus.mainloop()