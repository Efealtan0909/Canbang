import tkinter as tk

Window = tk.Tk()

Canvas = tk.Canvas(
	Window,
	width=500,
	height=500,
	cursor="none",
	bg="lightblue"
)

Canvas.pack()

Window.mainloop()