from tkinter import *
def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
    # abel.place(x=label.winfo_x(), y=label.winfo_y() - 10)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)
def move_right(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def move_left(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())
root=Tk()
root.geometry("700x500")

root.title("yared")
images=PhotoImage(file="one.png")
root.bind("<u>",move_up)
root.bind("<d>",move_down)
root.bind("<l>",move_left)
root.bind("<r>",move_right)


label=Label(root,image=images)
label.place(x=0,y=0)
root.mainloop()