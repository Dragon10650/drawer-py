from tkinter import *
import tkinter
import turtle

tk=Tk()
tki=tkinter

def buttonClck():
    b.place(x=1000,y=1500,width=2,height=12)
    b_forward=tki.Button(bg='red',text='⏫',command=Forward).place(x=150,y=50,width=32,height=32)
    b_backward=tki.Button(bg='blue',text='⏬',command=Backward).place(x=150,y=100,width=32,height=32)
    b_right=tki.Button(bg='yellow',text='⏩',command=Right).place(x=250,y=100,width=32,height=32)
    b_left=tki.Button(bg='green',text='⏪',command=Left).place(x=50,y=100,width=32,height=32)
    b_up=tki.Button(bg='white',text=' ',command=Up).place(x=100,y=100,width=32,height=32)
    b_down=tki.Button(bg='black',fg='white',text='•',command=Down).place(x=200,y=100,width=32,height=32)
    b_result=tki.Button(bg='grey',text='Результат',command=Result).place(x=132.5,y=150,width=64,height=32)
    b_clear=tki.Button(bg='pink',text='Стереть',command=Clear).place(x=132.5,y=200,width=64,height=32)
    
def Forward():
    t.forward(10)

def Backward():
    t.backward(10)

def Right():
    t.right(90)

def Left():
    t.left(90)

def Up():
    t.up()

def Down():
    t.down()
    
def Result():
    tk.destroy()
    t.hideturtle()

def Clear():
    t.clear()
    t.up()
    t.goto(0,0)
    t.down()
    
tk.title('Управление')
tk.geometry('500x300')
b=tki.Button(text='Начать',command=buttonClck)
b.place(x=250,y=150,width=64,height=64)

t=turtle.Pen()
turtle.title('Холст')

input()
