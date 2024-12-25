from tkinter import *

# Variables
current_x = 0
current_y = 0
def locate_xy(event):
  global current_x, current_y
  current_x, current_y = event.x, event.y
  print(current_x, current_y) 

def addline(event):
  global current_x, current_y
  print(current_x, current_y, event.x, event.y)
  canvas.create_line((current_x, current_y, event.x,event.y))
  current_x, current_y = event.x, event.y
# Create a window
window = Tk()
window.title("Paint made with the tkinter libary for Python")
window.state("normal")
window.geometry("1280x720")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# Create a canvas
canvas = Canvas(window)
canvas.grid(row=0, column=0, sticky="nsew")

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addline)

#Colors!!
canvas.create_rectangle((10, 10, 30, 30), fill="black")
canvas.create_rectangle((10, 80, 30, 30), fill="gray")
#canvas.create_line(20, 20, 80, 60)
# Main Loop
window.mainloop()