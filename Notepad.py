from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox as mas
import pyautogui as auto
from tkinter import filedialog as fd
import pyqrcode
# *******import pypng for save the qrcode**********
import os
from os import path
from tkinter.font import Font
import time
#=========================\\\\Code is start here////========================
gu = Tk()
gu.title('Sourav Editor')
x,y = auto.size()
gu.geometry("800x400")
gu.maxsize(x,y)
gu.minsize(200,200)
# gu.wm_iconbitmap("e:/mY ICO.ico")

scr = Scrollbar(gu)#Scrollbar vartical add
scr.pack(fill="y", side=RIGHT)

#-----------------Text Editor is start now here------------
fon = Font(size=12)
t = Text(gu, bg='#333333',fg="white", font=fon, yscrollcommand=scr.set)
t.pack(fill=BOTH, expand=TRUE)
t.config(insertbackground='white')#Cursor color
scr.config(command=t.yview)

#=========================Edit menu functions=====================
def cut():
    t.event_generate(('<<Cut>>'))
def copy():
    t.event_generate(('<<Copy>>'))
def past():
    t.event_generate(('<<Paste>>'))
def fs():
    def fsize():
        size = u.get()
        if size == "":
            auto.alert(text="Please Enter some value")
        else:
            if int(size) > 100:
                auto.alert(text="Maxsize is 100")
            elif int(size) < 10:
                auto.alert(text="Minsize is 10")
            else:
                fon.config(size=size)
                gu1.destroy()
        
    gu1 = Toplevel()
    gu1.transient(gu)
    gu1.title('Font Size')
    gu1.geometry("350x100")
    gu1.maxsize(350,100)
    gu1.minsize(350,100)
    gu1.config(bg="#333333")
    Label(gu1,text="Enter Your Font Size:", bg="#333333", fg="white").pack()
    u = Entry(gu1,width=40)
    u.pack()
    Label(gu1,text="", bg="#333333").pack()
    btn1 = Button(gu1,text="Ok", width=10, command=fsize, bg="white")
    btn1.pack()
#==================Format menu Background color functions=============
def white():
    t.config(bg="white",fg="black")
    t.config(insertbackground='black')
def defult():
    t.config(bg="#333333",fg="white")
    t.config(insertbackground='white')
def custom():
    color = colorchooser.askcolor(title="Background Color")
    t.config(bg=color[1])
#=====================Format menu Font color functions=================
def defutlfont():
    t.config(bg="#333333", fg="white")
    t.config(insertbackground='white')
def customfont():
    color = colorchooser.askcolor(title="Font Color")
    t.config(fg=color[1])  
def screen(ev=""):#.......Screenshot function..................
    def shot():
        fname = u.get()    
        if fname == "":
            auto.alert(text="Please Enter Your File Name")          
        else:
            gu1.destroy()
            os.chdir('c:/Screenshot')
            checkfile = path.isfile(f'{fname}.png')
            if checkfile is True:
                auto.alert(text="This name is already exits enter difarent name!!")
            else:
                time.sleep(1.5)
                auto.screenshot(f"c:/Screenshot/{fname}.png")
                auto.alert("Screenshot is Successfully Creat in\n 'C:\"Screenshot' Folder")
                
    os.chdir('c:/')
    check = path.isdir('Screenshot')
    if check == True:
        pass
    else:
        os.mkdir('Screenshot')
    gu1 = Toplevel()
    gu1.transient(gu)#This option for toplevel only cross button no max and min button
    gu1.title('Screenshot')
    gu1.geometry("350x100")
    gu1.maxsize(350,100)
    gu1.minsize(350,100)
    gu1.config(bg="#333333")
    Label(gu1,text="Enter Your File Name :", bg="#333333", fg="white").pack()
    u = Entry(gu1,width=40)
    u.pack()
    Label(gu1,text="", bg="#333333").pack()
    btn1 = Button(gu1,text="Ok", width=10, command=shot, bg="white")
    btn1.pack()          
#=====================File menu functions========================
def Exit(event):#........exit function........
    x = auto.confirm("Do you want to save", "Location")
    if x == "OK":
        save()
    else:
        gu.destroy()
#if click cancel button so cancel function is run


def Open(event=""):#......open function........
    f = fd.askopenfile(title='Save File',filetypes=(("All Files",".*"),("Text Fils",".*")))
    if f is None:
        pass
    else:
        for word in f:
            t.insert(END,word)

def new(event=""):#....new option function.....
    t.delete(1.0, END)

def save(event=""):#......save function.........
    f = fd.asksaveasfile(mode="w", title='Save File', defaultextension=".txt", filetypes=(("All Files",".*"),("Text Fils",".*")))
    # print(f)
    if f is None:
        pass
    else:
        getT = t.get(1.0, END)
        f.write(getT)
        f.close()

def saveq():#......QR code save function........
    def qrcom():
        fname = u.get()
        if fname == "":
            auto.alert(text="Please Enter Your File Name")
        else:
            gu1.destroy()
            os.chdir('c:/QrCode')
            checkfile = path.isfile(f'{fname}.png')
            if checkfile is True:
                auto.alert(text="This name is already exits enter difarent name!!")
            else:
                # try:
                fetch = t.get(1.0, END)
                P=pyqrcode.create(fetch)
                P.png(f"c:/QrCode/{fname}.png", scale=8)
                auto.alert("QR code is Successfully Creat in\n 'C:\"QRCode' Folder")
                # except:
                    # auto.alert("Somthing is wrong here", "Screenshot")
                
    os.chdir('c:/')
    check = path.isdir('QrCode')
    if check == True:
        pass
    else:
        os.mkdir('QrCode')

    gu1 = Toplevel()
    gu1.transient(gu)
    gu1.title('Enter Your File Name')
    gu1.geometry("350x100")
    gu1.maxsize(150,100)
    gu1.minsize(350,100)
    gu1.config(bg="#333333")
    Label(gu1,text="Enter Your File Name:", bg="#333333", fg="white").pack()
    u = Entry(gu1,width=40)
    u.pack()
    Label(gu1,text="", bg="#333333").pack()
    btn1 = Button(gu1,text="Ok", width=10, command=qrcom)
    btn1.pack()

#This is cancel function
def cancel(event=""):
    x = mas.askyesno( "Confirm", "Do you want to save")
    if x == True:
        save()
    else:
        gu.destroy()
#if click cancel button so cancel function is run
gu.protocol('WM_DELETE_WINDOW', cancel)

#=======================Menu Bar is start now here====================
menu = Menu(gu)
fm = Menu(menu, tearoff=0)#bg="#333333", fg="white")#file menu..........
fm.add_command(label="New         Ctrl+N", command=new)
gu.bind('<Control-N>', new)
gu.bind('<Control-n>', new)
fm.add_command(label="Open       Ctrl+O", command=Open)
gu.bind('<Control-O>', Open)
gu.bind('<Control-o>', Open)
fm.add_command(label="Save         Ctrl+S", command=save)
gu.bind('<Control-S>', save)
gu.bind('<Control-s>', save)
fm.add_separator()
fm.add_command(label="Save As QRCode", command=saveq)
fm.add_separator()
fm.add_command(label="Exit           Ctrl+E", command=cancel)
gu.bind('<Control-e>', Exit)
gu.bind('<Control-E>', Exit)
menu.add_cascade(label="File", menu=fm)

em = Menu(menu, tearoff=0)#Edit menu..........................
em.add_command(label="Copy     Ctrl+C", command=copy)
em.add_command(label="Cut        Ctrl+X", command=cut)
em.add_command(label="Past       Ctrl+V", command=past)
em.add_separator()
em.add_command(label="Screenshot       Alt+S", command=screen)
gu.bind('<Alt-s>', screen)
gu.bind('<Alt-S>', screen)
menu.add_cascade(label="Edit", menu=em)

Format = Menu(menu, tearoff=0)#Format menu........................
forBg = Menu(Format, tearoff=0)#<=====Background_color=======
forBg.add_command(label="White", command=white)
forBg.add_command(label="Defult", command=defult)
forBg.add_command(label="Custom", command=custom)
Format.add_cascade(label="Background Color", menu=forBg)
Format.add_separator()
fg = Menu(Format, tearoff=0) #<========Font_color========
fg.add_command(label="Defult", command=defutlfont)
fg.add_command(label="Custom", command=customfont)
Format.add_cascade(label="Font Color", menu=fg)
Format.add_command(label="Font Size", command=fs)#<=======Font size menu======
menu.add_cascade(label="Format", menu=Format)

menu.add_command(label="Help")
gu.config(menu=menu)


gu.mainloop()