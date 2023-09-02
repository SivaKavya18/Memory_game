
from tkinter import *
from PIL import Image,ImageTk,ImageOps
import random
from tkinter import ttk,messagebox
root = Tk()
root.title('Memory Game')
root.geometry("1075x1075")
img=ImageTk.PhotoImage(Image.open(r"main.png"))
img1=ImageTk.PhotoImage(Image.open(r"Doreamon.jpg"))
img2=ImageTk.PhotoImage(Image.open(r"Jerry.png"))
img3=ImageTk.PhotoImage(Image.open(r"kungfu.jpg"))
img4=ImageTk.PhotoImage(Image.open(r"panda.png"))
img5=ImageTk.PhotoImage(Image.open(r"powepuff.jpg"))
img6=ImageTk.PhotoImage(Image.open(r"Shinchan.jpg"))
li_img=[img1,img2,img3,img4,img5,img6]
li_ord=[0,1,2,3,4,5,0,1,2,3,4,5]
random.shuffle(li_ord)
match_list=[]
co=6
def fun(i,im):
    global co,button_dict
    button_dict[i].configure(image=im)
    button_dict[i].image=im 
    match_list.append(i)
    print(match_list)
    print(button_dict[i].image)
    def fun2(ma):
        global co
        if (len(match_list)==2):
            if (li_ord[match_list[0]]==li_ord[match_list[1]]):
                print('matched')
                button_dict[match_list[0]].destroy()
                button_dict[match_list[1]].destroy()
                co=co-1
                print(co)
                if (co==0):
                    messagebox.showinfo('memory game','Completed')
                    print('Completed')
            else:
                button_dict[match_list[0]]['image']=img 
                button_dict[match_list[1]]['image']=img 
                print('unmatched')
            match_list.clear()
    root.after(1500,lambda:fun2(match_list))

button_dict={}
i=0
for item in li_ord:
    def func(i=i,im=li_img[li_ord[i]]):
        return fun(i,im)
    button_dict[i]=Button(root, width=200,image=img ,height=200,command=func)
    button_dict[i].place(y=((i)//4)*215,x=((i)%4)*215)
    i=i+1

button = Button(root, width=200,image=img ,command=fun, height=200)

root.mainloop()
