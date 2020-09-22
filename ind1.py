import tkinter
from tkinter import *
from PIL import ImageTk, Image

root=Toplevel()
root.geometry("1400x700+0+0")
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="food.png")
canvas.create_image(0,0, anchor=NW, image=img)

def chole():
    import cholebh
    
b11 = Button(root,text=' CHOLE BHATURE  ',cursor="hand2",command=chole,activebackground='ivory2',bg='black',fg='white',width=15,borderwidth=3,font=('bazooka  20  bold '),padx=5,pady=10,relief=RAISED)
b11.place(x=460,y=85)

def dal():
    import daal

b22 = Button(root,text=' DAL MAKKHANI ',cursor="hand2",command=dal,activebackground='ivory2',bg='black',fg='white',width=15,borderwidth=3,font=('bazooka 20  bold '),padx=5,pady=10,relief=RAISED)
b22.place(x=460,y=200)

def kadhai():
    import paneer
  
b33 = Button(root,text=' KADAI PANEER  ',cursor="hand2",command=kadhai,activebackground='ivory2',bg='black',fg='white',width=15,borderwidth=3,font=('bazooka  20  bold '),padx=5,pady=10,relief=RAISED)
b33.place(x=460,y=315)

def saag():
    import sarso

b44 = Button(root,text=' SARSO KA SAAG ',cursor="hand2",command=saag,activebackground='ivory2',bg='black',fg='white',width=15,borderwidth=3,font=('bazooka  20  bold '),padx=5,pady=10,relief=RAISED)
b44.place(x=460,y=430)

def kheer():
    import kher

b55= Button(root,text=' KHEER  ',command=kheer,cursor="hand2",activebackground='ivory2',bg='black',fg='white',width=15,borderwidth=3,font=('bazooka  20 bold '),padx=5,pady=10,relief=RAISED)
b55.place(x=460,y=545)    

root.mainloop()



