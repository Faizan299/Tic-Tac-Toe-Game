import tkinter .messagebox
from tkinter import *

root=Tk()
root.geometry("1150x750")
root.title("Tic Tac Toe Game")
root.configure(bg='black')


Tops=Frame(root,bg='black',pady=2,width=1350,height=100,relief=RIDGE)
Tops.grid(row=0,column=0)

title=Label(Tops,font=('Algerian',30,'bold'),text="Tic Tac Toe Game",bd=21,bg='black',fg='white',justify=CENTER)
title.grid(row=0,column=0)

mainframe=Frame(root,bg='blue',bd=10,width=1350,height=600,relief=RIDGE)
mainframe.grid(row=1,column=0)

left=Frame(mainframe ,bd=10,width=750,height=500,pady=2,padx=10,bg='grey',relief=RIDGE)
left.pack(side=LEFT)

right=Frame(mainframe ,bd=10,width=560,height=500,padx=10,pady=2,bg='grey',relief=RIDGE)
right.pack(side=RIGHT)

right1=Frame(right ,bd=10,width=560,height=200,padx=10,pady=2,bg='grey',relief=RIDGE)
right1.grid(row=0,column=0)

right2=Frame(right ,bd=10,width=560,height=200,padx=10,pady=2,bg='grey',relief=RIDGE)
right2.grid(row=1,column=0)

playerX=IntVar()
playerO=IntVar()

playerX.set(0)
playerO.set(0)

button=StringVar()
click = True


def checker(button):
    global click
    if button["text"] == " " and click ==True:
        button["text"] = "X"
        click = False
        score()

    elif button["text"] == " " and click ==False:
        button["text"] = "O"
        click = True
        score()

def score():
    if(button1["text"]=='X' and button2["text"]=='X' and button3["text"]=='X'):
        button1.configure(background='green')
        button2.configure(background='green')
        button3.configure(background='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button1["text"]=='X' and button4["text"]=='X' and button7["text"]=='X'):
        button1.configure(background='green')
        button4.configure(background='green')
        button7.configure(background='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button1["text"]=='X' and button5["text"]=='X' and button9["text"]=='X'):
        button1.configure(background='green')
        button5.configure(background='green')
        button9.configure(background='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button3["text"]=='X' and button5["text"]=='X' and button7["text"]=='X'):
        button3.configure(background='green')
        button5.configure(background='green')
        button7.configure(background='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button2["text"]=='X' and button5["text"]=='X' and button8["text"]=='X'):
        button2.configure(background='green')
        button5.configure(background='green')
        button8.configure(background='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button3["text"]=='X' and button6["text"]=='X' and button9["text"]=='X'):
        button3.configure(background='green')
        button6.configure(background='green')
        button9.configure(background='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button4["text"]=='X' and button5["text"]=='X' and button6["text"]=='X'):
        button4.configure(background='green')
        button5.configure(background='green')
        button6.configure(background='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button7["text"]=='X' and button8["text"]=='X' and button9["text"]=='X'):
        button7.configure(bg='green')
        button8.configure(bg='green')
        button9.configure(bg='green')
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button1["text"]=='O' and button2["text"]=='O' and button3["text"]=='O'):
        button1.configure(bg='green')
        button2.configure(bg='green')
        button3.configure(bg='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have just won a game")

    if(button1["text"]=='O' and button4["text"]=='O' and button7["text"]=='O'):
        button1.configure(background='green')
        button4.configure(background='green')
        button7.configure(background='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button2["text"]=='O' and button5["text"]=='O' and button8["text"]=='O'):
        button2.configure(background='green')
        button5.configure(background='green')
        button8.configure(background='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button1["text"]=='O' and button5["text"]=='O' and button9["text"]=='O'):
        button1.configure(background='green')
        button5.configure(background='green')
        button9.configure(background='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button3["text"]=='O' and button5["text"]=='O' and button7["text"]=='O'):
        button3.configure(background='green')
        button5.configure(background='green')
        button7.configure(background='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button3["text"]=='O' and button6["text"]=='O' and button9["text"]=='O'):
        button3.configure(background='green')
        button6.configure(background='green')
        button9.configure(background='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won a game")

    if(button4["text"]=='O' and button5["text"]=='O' and button6["text"]=='O'):
        button4.configure(bg='green')
        button5.configure(bg='green')
        button6.configure(bg='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have just won a game")

    if(button7["text"]=='O' and button8["text"]=='O' and button9["text"]=='O'):
        button7.configure(bg='green')
        button8.configure(bg='green')
        button9.configure(bg='green')
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O","You have just won a game")
        

def reset():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(background='skyblue')
    button2.configure(background='skyblue')
    button3.configure(background='skyblue')
    button4.configure(background='skyblue')
    button5.configure(background='skyblue')
    button6.configure(background='skyblue')
    button7.configure(background='skyblue')
    button8.configure(background='skyblue')
    button9.configure(background='skyblue')

def Newgame():
    reset()
    playerX.set(0)
    playerO.set(0)

plyx=Label(right1,font=('Brush Script MT',30,'bold'),text="Player X",padx=2,pady=2,bg='grey')
plyx.grid(row=0,column=0,sticky=W)

pxent=Entry(right1,font=('Brush Script MT',20,'bold'),bd=2,fg='black',textvariable=playerX,width=14,justify=LEFT).grid(row=0,column=1)

plyo=Label(right1,font=('Brush Script MT',30,'bold'),text="Player O",padx=2,pady=2,bg='grey')
plyo.grid(row=1,column=0,sticky=W)
p0ent=Entry(right1,font=('Brush Script MT',20,'bold'),bd=2,fg='black',textvariable=playerO,width=14,justify=LEFT).grid(row=1,column=1)

btnreset=Button(right2,text="Reset",font=('Brush Script MT' ,26 , 'bold'),width=8,bg='gainsboro',command=reset)
btnreset.grid(row=0,column=0)

btnnew=Button(right2,text="New",font=('Brush Script MT' ,26 , 'bold'),width=8,bg='gainsboro',command=Newgame)
btnnew.grid(row=1,column=0)

button1=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button1))
button1.grid(row=1,column=0)

button2=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button2))
button2.grid(row=1,column=1)

button3=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button3))
button3.grid(row=1,column=2)

button4=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button4))
button4.grid(row=2,column=0)

button5=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button5))
button5.grid(row=2,column=1)

button6=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button6))
button6.grid(row=2,column=2)

button7=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button7))
button7.grid(row=3,column=0)

button8=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button8))
button8.grid(row=3,column=1)

button9=Button(left,text=" ",font=('Times' ,30 , 'bold'),height=3,width=8,bg='skyblue',command=lambda:checker(button9))
button9.grid(row=3,column=2)

root.mainloop()
