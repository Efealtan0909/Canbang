import tkinter as tk

Window = tk.Tk()
Window.title('Canbang')

WIDTH = HEIGHT = 400
x1 = y1 = WIDTH / 2

Canvas = tk.Canvas(
    Window,
    width=WIDTH,
    height=HEIGHT
)

# TODO: make button start the game
Button = tk.Button(
    text="Click to Start the Game",
    command="StartGame",
    width=25,
    height=5,
    bg="green",
    fg="white",
)

# Functions

# TODO: make moving work
def move(event):
    global x1, y1
    if event.char == "w":
    y1 += 1
    pass
    if event.char == "a":   
    x1 += 1
    pass
    if event.char == "s":
    y1 -= 1
    pass
    if event.char == "d":
    x1 -= 1
    pass
pass
# TODO: draw function
# TODO: make movements work
# TODO: add random can spawner



canvas.pack()
Button.pack()

Window.mainloop()