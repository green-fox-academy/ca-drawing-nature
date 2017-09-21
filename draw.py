from tkinter import *

root = Tk()

canvas = Canvas(root, width='400', height='400', bd=0, highlightthickness=0)
canvas.pack()

canvas.create_oval(0, 0, 10, 10, fill='red', width=0)

root.mainloop()
