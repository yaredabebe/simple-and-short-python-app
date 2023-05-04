from  tkinter import *
from  time import*
def the_Time():
    ti = strftime(" %H: %M: %S %p")
    label_time.config(text=ti)

    day=strftime("%A")
    day_label.config(text=day)

    year = strftime("%B, %Y")
    date_label.config(text=year)
    al = strftime("%c")
    day_label.config(text=al)
    root.after(1000,the_Time)


root=Tk()
label_time=Label(root,font=("Arial",33),fg="#7FFF00",bg="black")
label_time.pack()
day_label = Label(root,font=("Ink Free",25,"bold"),fg="#7FFF00")
day_label.pack()

date_label = Label(root,font=("Ink Free",30,"bold"),fg="#CD1076")
date_label.pack()
the_Time()
root.mainloop()