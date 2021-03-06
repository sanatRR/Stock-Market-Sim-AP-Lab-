#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Nov 23, 2021 02:54:22 PM IST  platform: Windows NT

import sys
from tkinter import *      
from PIL import ImageTk,Image

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Stock_Price_Name_support
import classes.net_connect
from classes.database import *

def buy(email,symbol):
    current_balance = person_operations(email,1)
    current_stock_balance = transaction_operations(email,0,symbol)
    quote = classes.net_connect.get_quote(symbol)

    if(current_balance<quote):
        Label(root,text="LOW BALANCE",height="2", width="15", font=("Comic Sans MS", 13)).pack()

        #Label showing Low balance error
        pass
    else:
        new_balance = current_balance-quote
        transaction_operations(email,1,symbol,1,quote,1)
        person_operations(email,0,new_balance)
        current_exp = person_operations(email,5)
        set_exp = current_exp+quote
        person_operations(email,4,set_exp)

def sell(email,symbol):
    current_balance = person_operations(email,1)
    current_stock_balance = transaction_operations(email,0,symbol)
    quote = classes.net_connect.get_quote(symbol)

    if current_stock_balance == 0:
        Label(root,text="NOT ENOUGH STOCKS",height="2", width="30", font=("Comic Sans MS", 13)).pack()

        #Label showing Low stock balance error
        pass
    else:
        new_balance = current_balance+quote
        transaction_operations(email,1,symbol,-1,quote,1)
        person_operations(email,0,new_balance)
        current_gain = person_operations(email,3)
        set_gain = current_gain+quote
        person_operations(email,2,set_gain)




def vp_start_gui(email,symbol):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    stock_symbol = symbol
    top = Toplevel1 (width,height,email,stock_symbol,root)
    Stock_Price_Name_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Stock_Price_Name_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self,width,height,email,stock_symbol, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        

        top.geometry("%dx%d" % (width,height))
        # top.minsize(120, 1)
        # top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Canvas1 = tk.Canvas(top)
        image = Image.open("plot.png")
        self.img = ImageTk.PhotoImage(image,master=self.Canvas1)
        self.Canvas1.create_image(0,0,anchor=NW,image=self.img)
        self.Canvas1.place(relx=0.049, rely=0.19, relheight=0.70, relwidth=0.45)
        self.Canvas1.configure(background="#d9d9d9")
      #  self.Canvas1.configure(file="plot.png")
        self.Canvas1.configure(borderwidth="4")
        self.Canvas1.configure(cursor="fleur")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
    


        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.583, rely=0.489, height=44, width=147)
        self.Button1.configure(activebackground="#05fa24")
        self.Button1.configure(activeforeground="#22fd02")
        self.Button1.configure(background="#05fa2b")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''BUY''',command=lambda:buy(email,stock_symbol))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.583, rely=0.689, height=44, width=147)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#f81307")
        self.Button2.configure(cursor="fleur")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''SELL''',command = lambda:sell(email,stock_symbol))

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.583, rely=0.178, height=41, width=144)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 13")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text="NAME: "+stock_symbol)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.567, rely=0.311, height=31, width=164)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text="PRICE: "+str(classes.net_connect.get_quote(stock_symbol)))

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.033, rely=0.044, height=51, width=214)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(cursor="arrow")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 17")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''BUY/SELL STOCKS''')

if __name__ == '__main__':
    vp_start_gui()





