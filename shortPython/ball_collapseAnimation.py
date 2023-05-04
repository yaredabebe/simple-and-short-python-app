from tkinter import *
import time
from ball import *
xv=1
yv=2
W=900
H=700

root=Tk()
canvas=Canvas(root,width=W,height=H)
canvas.pack()
volley = Ball(canvas,0,0,7,8,"white",80)
bingball=Ball(canvas,0,0,2,3,"yellow",80)
poopball=Ball(canvas,0,0,3,2,"green",80)
dooball=Ball(canvas,0,0,4,5,"black",80)


try:
    while True:
        volley.move()
        poopball.move()
        bingball.move()
        dooball.move()
        root.update()
        time.sleep(0.01)
except:
    print("game over")

root.mainloop()