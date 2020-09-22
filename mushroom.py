import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Toplevel()
root.geometry("1400x700+0+0")
root.config(bg='white')
canvas = Canvas(root, width =500, height=500)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
img = ImageTk.PhotoImage(file="mush1.jpg")
canvas.create_image(1190,37,anchor=NW ,image=img)

label=Label(root,text="MUSHROOM RISOTTO",font="Helvetica 15 bold",pady=3,padx=3,bd=2,fg='white',bg='black',relief=RAISED)
label.place(x=0,y=2,relwidth=1)

t=tk.Text(root,bg='white',fg='black',font="Helvetica 10 bold")
t.place(x=2,y=37,height=669,width=800)
quote=""" 
                    RECIPE OF MUSHROOM RISOTTO

STEP 1
Put 50g dried porcini mushrooms into a large bowl and pour over 1 litre boiling water. Soak for 20 mins,
then drain into a bowl, discarding the last few tbsp of liquid left in the bowl.

STEP 2
Crumble 1 vegetable stock cube into the mushroom liquid, then squeeze the mushrooms gently to remove any
liquid.

STEP 3
Heat 2 tbsp olive oil in a shallow saucepan or deep frying pan over a medium flame. Add 1 finely chopped
onion and 2 finely chopped garlic cloves, then fry for about 5 mins until soft.

STEP 4
Stir in 250g chopped chestnut mushrooms and the dried mushrooms, season with salt and pepper and continue
to cook for 8 mins until the fresh mushrooms have softened.

STEP 5
Tip 300g risotto rice into the pan and cook for 1 min. Pour over a 175ml glass of white wine and let it
bubble to nothing so the alcohol evaporates.

STEP 6
Keep the pan over a medium heat and pour in a quarter of the mushroom stock. Simmer the rice, stirring often,
until the rice has absorbed all the liquid.

STEP 7
Add about the same amount of stock again and continue to simmer and stir - it should start to become creamy,
plump and tender. By the time the final quarter of stock is added, the rice should be almost cooked.

STEP 8
Continue stirring until the rice is cooked. If the rice is still undercooked, add a splash of water. Take the
pan off the heat, add 25g butter and scatter over 25g grated parmesan or Grana Padano cheese and half a handful
of chopped parsley leaves.

STEP 9
Cover and leave for a few mins so that the rice can take up any excess liquid as it cools a bit. Give the risotto
a final stir, spoon into bowls and scatter with the remaining 25g grated cheese and the remaining chopped parsley
leaves.



          

"""
t.insert(tk.END,quote)
t.config(state="disabled")

t1=tk.Text(root,bg='white',fg='black',font="Helvetica 9 bold")
t1.place(x=803,y=37,height=204,width=425)
quote1="""
ABOUT THE DISH:

Mushroom Risotto Recipe is a classic Italian classic dish made with
creamy arborio rice and sauteed mushrooms. Typically, risotto is
slowly cooked in a broth of vegetable/chicken adding it in intervals
till the arborio rice is fluffed up and creamy. This slow cooking
method helps to release the starch from the rice, giving risotto its
characteristic silky, creamy texture.Addition of mushroom makes this
risotto more healthy and tasty. Do try this easy cheesy creamy mushroom
risotto recipe along with Quick Bread Pizza for dinner!



"""

t1.insert(tk.END,quote1)
t1.config(state="disabled")
t2=tk.Text(root,bg='white',fg='black',font="Helvetica 14 bold")
t2.place(x=803,y=238,height=462,width=625)
quote2="""

INGREDIENTS:

- 50g dried porcini mushrooms
- 1 vegetable stock cube
- 2 tbsp olive oil
- 1 onion, finely chopped
- 2 garlic cloves, finely chopped
- 250g pack chestnut mushrooms, chopped
- 300g risotto rice, such as arborio
- 1 x 175ml glass white wine
- 25g butter
- handful parsley leaves, chopped
- 50g parmesan or Grana Padano, freshly grated

"""

t2.insert(tk.END,quote2)
t2.config(state="disabled")



tk.mainloop()





