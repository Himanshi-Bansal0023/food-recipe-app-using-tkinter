import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Toplevel()
root.geometry("1400x700+0+0")
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="mexicanimg.jpg")
canvas.create_image(0,0, anchor=NW, image=img)

def mexic():
    import bbq
    
b11 = Button(root,text='EASY BBQ BEANS',cursor="hand2",command=mexic,activebackground='ivory2',bg='black',fg='white',width=20,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b11.place(x=500,y=85)

def cakes():
    import pancakes


b22 = Button(root,text='QUESADILLA PANCAKES',cursor="hand2",command=cakes,activebackground='ivory2',bg='black',fg='white',width=20,borderwidth=3,font=('bazooka 15  bold '),padx=5,pady=10,relief=RAISED)
b22.place(x=500,y=200)

def soup():
    import soup
b33 = Button(root,text='SWEET POTATO SOUP',cursor="hand2",command=soup,activebackground='ivory2',bg='black',fg='white',width=20,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b33.place(x=500,y=315)

def rice():
    import rice

b44 = Button(root,text=' MAXICAN RED RICE  ',cursor="hand2",command=rice,activebackground='ivory2',bg='black',fg='white',width=20,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b44.place(x=500,y=430)

def corn():
    import salsa

b55= Button(root,text='CORN & PEPPER SALSA  ',cursor="hand2",command=corn,activebackground='ivory2',bg='black',fg='white',width=20,borderwidth=3,font=('bazooka  15 bold '),padx=5,pady=10,relief=RAISED)
b55.place(x=500,y=545)    

root.mainloop()
