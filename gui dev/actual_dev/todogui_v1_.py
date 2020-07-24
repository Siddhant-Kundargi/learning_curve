from datetime import date
from tkinter import *

today_date = date.today()
today_list = [today_date]


def add_new():
    today_list.append(e.get())

def clear_list():
    today_list.clear()

def activity_completed():
    today_list.remove(e)

def correction_to_the_list():
    tr = Entry(root,text="activity to replace")
    tr.grid(row=8,column=1)
    today_list.remove(tr)
    drg = Entry(root,text="new task")
    drg.grid(row=8,column=1)
    today_list.append(drg)

def SHow():
    rwn=9
    for element in today_list:
        labelps = Label(root,text = element)
        labelps.grid(row=rwn,column=2)
        rwn += 1


        
    
root = Tk()

labelp1 = Label(root,text = "Gui Todo list\n")
labelp1.grid(row=1,column=2)


e = Entry(root,text="new/remove")
e.grid(row=4,column=1)

AddButton = Button(root,text="Add New",command=add_new)
AddButton.grid(row=5,column=1)

rem_button = Button(root,text="remove/Completed Activity",command=activity_completed)
rem_button.grid(row=5,column=2)

rep_button = Button(root,text="replace",command=correction_to_the_list)
rep_button.grid(row=6,column=1)

show_button = Button(root,text="Show",command=SHow)
show_button.grid(row=6,column=2)

cll_button = Button(root,text="clean list",command=clear_list)
cll_button.grid(row=7,column=1)

root.mainloop()


