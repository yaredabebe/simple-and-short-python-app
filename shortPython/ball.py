class Ball:

    def __init__(self,canvas,x,y,xv,yv,color,diameter):
        self.canvas=canvas

        self.xv=xv
        self.yv=yv
        self.image=canvas.create_oval(x,y,diameter,diameter,fill=color)

#image_width = self.images.width()
 #   image_height = images.height()
    def move(self):
        cordinates = self.canvas.coords(self.image)
        print(cordinates)
        if (cordinates[2] > (self.canvas.winfo_width()) or cordinates[0] < 0):
            self.xv = -self.xv
        if (cordinates[3] > (self.canvas.winfo_height()) or cordinates[1] < 0):
            self.yv = -self.yv
        self.canvas.move(self.image, self.xv, self.yv)