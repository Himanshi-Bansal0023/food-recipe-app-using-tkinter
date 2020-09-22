import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Toplevel()
root.geometry("1400x700+0+0")
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="chinesee.jpg")
canvas.create_image(0,0, anchor=NW, image=img)

def manchu():
    import manchurian


b11 = Button(root,text='MANCHURIAN ',cursor="hand2",command=manchu,activebackground='ivory2',bg='black',fg='white',width=13,borderwidth=3,font=('bazooka  16  bold '),padx=5,pady=10,relief=RAISED)
b11.place(x=70,y=500)

def noodles():
    import chowmein


b22 = Button(root,text=' NOODLES',cursor="hand2",command=noodles,activebackground='ivory2',bg='black',fg='white',width=13,borderwidth=3,font=('bazooka 16  bold '),padx=5,pady=10,relief=RAISED)
b22.place(x=310,y=500)

def momos():
    import momo
  
b33 = Button(root,text='MOMOS  ',cursor="hand2",command=momos,activebackground='ivory2',bg='black',fg='white',width=13,borderwidth=3,font=('bazooka  16  bold '),padx=5,pady=10,relief=RAISED)
b33.place(x=550,y=500)

def chilli():
    import potato

b44 = Button(root,text=' CHILLI POTATO  ',cursor="hand2",command=chilli,activebackground='ivory2',bg='black',fg='white',width=13,borderwidth=3,font=('bazooka  16  bold '),padx=5,pady=10,relief=RAISED)
b44.place(x=790,y=500)

def roll():
    import rolls

b55= Button(root,text=' SPRING ROLL  ',cursor="hand2",command=roll,activebackground='ivory2',bg='black',fg='white',width=13,borderwidth=3,font=('bazooka  16 bold '),padx=5,pady=10,relief=RAISED)
b55.place(x=1030,y=500)    

root.mainloop()
