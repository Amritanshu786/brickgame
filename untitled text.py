from tkinter import *
from tkinter import messagebox
def malemessage():
    messagebox.showinfo("Success", "You have selected male as an option")
def femalemessage():
    messagebox.showinfo("Success", "You have selected female as an option")
def click_me():
    if i.get()==1:
        malemessage()
    else:
        femalemessage()

root = Tk()

i=IntVar()
r1 = Radiobutton(root,text="Male",variable=i,value=1)
r2 = Radiobutton(root, text="Female", variable=i, value=2)
r1.pack()
r2.pack()
button=Button(root, text="Click Me", command=click_me)
button.pack()

root.geometry("300x300+120+120")
root.mainloop()