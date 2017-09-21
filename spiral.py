from tkinter import *
from math import cos, sin, pi

root = Tk()

canvas = Canvas(root, width='400', height='400', bd=0, highlightthickness=0)
canvas.pack()


def create_point(r, angle, offsetX, offsetY):
    x = offsetX + r * cos(angle)
    y = offsetY + r * sin(angle)
    canvas.create_oval(x, y, x+10, y+10, fill='black', width=0)

def create_spiral(centerX, centerY):
    c = 5
    r = 100
    for i in range(500):
        angle = i * 137.5 * 180/pi
        r = c * i**0.5
        create_point(r, angle, centerX, centerY)

create_spiral(200,200)

root.mainloop()
