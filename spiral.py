from tkinter import *
from math import cos, sin, pi

root = Tk()

canvas = Canvas(root, width='400', height='400', bd=0, highlightthickness=0)
canvas.pack()

def create_point(r, angle, offsetX, offsetY):
    x = offsetX + r * cos(angle)
    y = offsetY + r * sin(angle)
    canvas.create_rectangle(x, y, x+2, y+2, fill='black', width=0)

def create_spiral(centerX, centerY, c):
    r = 0
    for i in range(30):
        angle = i * 137.5 * 180/pi
        r = c * i**0.5
        create_point(r, angle, centerX, centerY)

def flower( x, y, const ):
    if const < 1:
        return
    else:
        create_spiral(x-50,y,const)
        create_spiral(x,y,const)
        create_spiral(x,y-50,const)
        create_spiral(x+50,y,const)
        create_spiral(x,y+50,const)
        flower( x, y, const-1.5 )

flower(200, 200, 30)

root.mainloop()
