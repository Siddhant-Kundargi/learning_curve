from tkinter import *
from __MyFn_1__ import *
root = Tk()


mylabel1 = Label(root, text="The heading goes here")
mylabel2 = Label(root, text="just kiddin buddy")
mylabel3 = Label(root, text="                                             ")

mylabel1.grid(row=1,column=1)
mylabel2.grid(row=3,column=2)
mylabel3.grid(row=2,column=3)
root.mainloop()
