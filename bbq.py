import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="bbq1.jpg")
canvas.create_image(1220,37,anchor=NW ,image=img)

label=Label(root,text="EASY BBQ BEANS ",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t.place(x=2,y=37,height=669,width=800)
quote=""" 
                                RECIPE OF EASY BBQ BEANS 

Step 1                                                
Heat the oil in a small pan.

Step 2
Fry onion until starting to brown.

Step 3
Then add garlic and cook for 1 min.

Step 4
Add vinegar and sugar and

Step 5
Cook until onions are caramelised.

Step 6
Stir in beans, passata, Worcestershire sauce (if using) and

Step 7
Seasoning and simmer for 10-15 mins until thickened.

Step 8
Stir through coriander and serve.


"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 11 bold")
t1.place(x=803,y=37,height=204,width=425)
quote1="""
ABOUT THE DISH:

Mexican twist on an American classic! Mexican Baked
Beans with Chorizo are smoky,sweet, and spicy all
at once. They’re bursting with yummy flavor.This
recipe makes a TON, it’s cheap, and it’s freezable.
The beans are perfect as a side at your next BBQ
(like the Fourth of July),piled on toast.

"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=462,width=625)
quote2="""

INGREADIENTS:

-1 tbsp olive oil
-1 onion , thinly sliced
-2 garlic cloves , chopped
-1 tbsp white or red wine vinegar
-1 heaped tbsp soft brown sugar
-400g tin pinto beans , drained and rinsed
-400ml tub passata
-1 tsp Worcestershire sauce or vegetarian alternative
  (optional) small bunch coriander , chopped




"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()





