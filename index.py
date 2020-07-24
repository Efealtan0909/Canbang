from time import time, sleep
import tkinter as tk
import math

GAMEFPS = 60

class Loop():
	def __init__(self, root, fps, loop_func):
		self.root = root
		self.fps = fps
		self.loop_func = loop_func
		self.unlimited = self.fps == 'unlimited'
		if (self.unlimited):
			self.frame_delay = 0
		else:
			self.frame_delay = 1000/self.fps
		self.running = False
	def schedule(self, exec_time, loop_func):
		self.root.after(max(int(self.frame_delay - (time() - exec_time)), 0), loop_func)
	def start(self):
		if (self.running): pass
		delta = self.frame_delay
		if (self.unlimited):
			delta = 0.1
		time_delay = time()
		def loop():
			nonlocal delta
			nonlocal time_delay
			if (not self.running): pass
			exec_time = time()
			self.loop_func(delta)
			delta = time() - time_delay
			if (delta == 0): delta = 0.1
			time_delay = time()
			self.schedule(exec_time, loop)
		self.schedule(0, loop)
	def stop(self):
		if (not self.running): pass
		self.running = False

class Camara:
	x_rot = 0
	fview = 180
	def __init__(self, x_rot = 0, fview = 90):
		self.x_rot = x_rot
		self.fview = fview
	def perspective(self, rot):
		rot_diff = self.x_rot - rot
		return (rot_diff / self.fview) * 500

class CrossAir:
	def __init__(self, c):
		self.c = c
		self.x = 0
		self.y = 0
		self.width = 10
		self.height = 10
		self.shape = self.c.create_rectangle(self.x, self.y, self.width, self.height, outline="black", fill="black")
	
	def draw(self):
		self.c.coords(self.shape, self.x, self.y, self.x + self.width, self.y + self.height)

	def update(self, event):
		self.x = event.x
		self.y = event.y

class FPS:
	def __init__(self, c):
		self.c = c
		self.x = 0
		self.y = 0
		self.fps = GAMEFPS
		self.text = tk.StringVar()
		self.text.set(self.fps)
		self.label = tk.Label(self.c, textvariable=self.text, fg="white", bg="black")
		self.label.place(x=self.x, y=self.y)
	def update(self):
		self.text.set(self.fps)

if __name__ == "__main__":
	Window = tk.Tk()
	Window.title('Canbang')

	Canvas = tk.Canvas(
		Window,
		width=500,
		height=500,
		bg="lightblue"
	)

	cam = Camara()

	crossair = CrossAir(Canvas)
	fpscounter = FPS(Canvas)
	def callback(e):
		cam.x_rot = (360/500) * e.x
		crossair.y = e.y
	Window.bind('<Motion>', callback)

	Canvas.pack()

	def loop(delta):
		fps = int(1/delta)
		cords = cam.perspective(0)
		crossair.x = cords
		crossair.draw()
		fpscounter.fps = fps

	gameloop = Loop(Window, GAMEFPS, loop)
	gameloop.start()

	Window.mainloop()