from tkinter import *
#variables
current_x = 0
current_y = 0
color = 'black'
def locate_xy(event):
  global current_x, current_y
  current_x = event.x
  current_y = event.y
def add_line(event):
  global current_x, current_y
 #print(current_x, current_y, event.x, event.y)
  canvas.create_line((current_x, current_y, event.x, event.y), fill = color)
  current_x = event.x
  current_y = event.y
def show_color(new_color):
  global color
  color = new_color


# Create a window
window = Tk()
window.title("Paint")
window.state("zoomed")
#Configure row
window.rowconfigure(0, weight=1)
#Configure column
window.columnconfigure(0, weight=1)

# Create a canvas
canvas = Canvas(window, bg="white")
canvas.grid(row=0, column=0, sticky="nsew")
canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', add_line)

def display_pallete():
  #Colors:)
  black = canvas.create_rectangle(10, 10, 30, 30, fill="black")
  grey = canvas.create_rectangle(10, 40, 30, 60, fill="gray")
  brown = canvas.create_rectangle(10, 70, 30, 90, fill="orange4")
  red = canvas.create_rectangle(10, 100, 30, 120, fill="red")
  orange =canvas.create_rectangle(10, 130, 30, 150, fill="orange")
  yellow = canvas.create_rectangle(10, 160, 30, 180, fill="yellow")
  green = canvas.create_rectangle(10, 190, 30, 210, fill="green")
  blue = canvas.create_rectangle(10, 220, 30, 240, fill="blue")
  purple = canvas.create_rectangle(10, 250, 30, 270, fill="purple")
  # Make the colors work
  canvas.tag_bind(black, "<Button-1>", lambda x: show_color("black"))
  canvas.tag_bind(grey, "<Button-1>", lambda x: show_color("gray"))
  canvas.tag_bind(brown, "<Button-1>", lambda x: show_color("orange4"))
  canvas.tag_bind(red, "<Button-1>", lambda x: show_color("red"))
  canvas.tag_bind(orange, "<Button-1>", lambda x: show_color("orange"))
  canvas.tag_bind(yellow, "<Button-1>", lambda x: show_color("yellow"))
  canvas.tag_bind(green, "<Button-1>", lambda x: show_color("green"))
  canvas.tag_bind(blue, "<Button-1>", lambda x: show_color("blue"))
  canvas.tag_bind(purple, "<Button-1>", lambda x: show_color("purple"))
display_pallete()
def new_canvas():
  canvas.delete("all")
  display_pallete()
# MenuBar
menubar = Menu(window)
window.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Canvas", command = new_canvas)
#anvas.create_line(20, 20, 80, 80, fill="red")
#MainLoop
window.mainloop()
