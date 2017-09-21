from tkinter import *
from math import cos, sin, pi

root = Tk()

canvas = Canvas(root, width='400', height='400', bd=0, highlightthickness=0)
canvas.pack()

r = 100

def create_point(angle,offsetX,offsetY):
    x = offsetX + r * cos(angle)
    y = offsetY + r * sin(angle)
    canvas.create_oval(x, y, x+10, y+10, fill='red', width=0)

angle = 0
n = 0
c = 8.6

for i in range(500):
    angle = i * 137.5 * 180/pi
    r = c * i**0.5
    create_point(angle, 200, 200)

root.mainloop()
