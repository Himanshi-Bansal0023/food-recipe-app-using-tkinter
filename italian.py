import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Toplevel()
root.geometry("1400x700+0+0")
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="italian1.jpeg")
canvas.create_image(0,0, anchor=NW, image=img)

def pasta():
    import pasta


b11 = Button(root,text='MIXED SAUCE PASTA  ',cursor="hand2",command=pasta,activebackground='ivory2',bg='chartreuse3',fg='white',width=18,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b11.place(x=390,y=85)

def pizza():
    import pizza


b22 = Button(root,text=' MARGHERITA PIZZA ',cursor="hand2",command=pizza,activebackground='ivory2',bg='chartreuse3',fg='white',width=18,borderwidth=3,font=('bazooka 15  bold '),padx=5,pady=10,relief=RAISED)
b22.place(x=390,y=200)

def mush():
    import mushroom
  
b33 = Button(root,text=' MUSHROOM RISOTTO ',cursor="hand2",command=mush,activebackground='ivory2',bg='chartreuse3',fg='white',width=18,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b33.place(x=390,y=315)

def food():
    import lasagna

b44 = Button(root,text=' LASAGNA ',cursor="hand2",activebackground='ivory2',command=food,bg='chartreuse3',fg='white',width=18,borderwidth=3,font=('bazooka  15  bold '),padx=5,pady=10,relief=RAISED)
b44.place(x=390,y=430)

def food1():
    import bread
    
b55= Button(root,text=' GARLIC BREAD  ',cursor="hand2",command=food1,activebackground='ivory2',bg='chartreuse3',fg='white',width=18,borderwidth=3,font=('bazooka  15 bold '),padx=5,pady=10,relief=RAISED)
b55.place(x=390,y=545)    

root.mainloop()
