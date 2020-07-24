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
	def __init__(self, x_rot = 0, fview = 90):
		self.x_rot = x_rot
		self.fview = fview
	def perspective(self, rot):
		rot_diff = self.x_rot - rot
		return (rot_diff / self.fview) * 500

class Object:
	x_rot = 0
	y     = 0
	width = 10
	height= 10
	def __init__(self, scene, x_rot = 0, y = 0):
		self.scene = scene
		self.x_rot = x_rot
		self.y = y
	def draw(self, cords):
		if (not hasattr(self, 'shape')): pass
		x,y = cords
		return self.scene.c.coords(self.shape, x, y, x + self.width, y + self.height)
	def create(self, cords):
		x,y = cords
		self.shape = self.scene.c.create_rectangle(x, y, self.width, self.height)
		return self.shape

class Scene:
	objects = {}
	def __init__(self, c, camp = ()):
		self.c = c
		self.cam = Camara(*camp)
	def cords(self, obj):
		x = self.cam.perspective(obj.x_rot)
		y = obj.y
		return (x,y)
	def draw(self):
		for objid, obj in self.objects.items():
			obj.draw(self.cords(obj))
	def create(self, obj):
		if (hasattr(obj, 'shape')):
			self.c.delete(obj.shape)
			del self.objects[obj.shape]
			del obj.shape
		objid = obj.create(self.cords(obj))
		self.objects[objid] = obj
		return objid
	def make(self, obj, *p, **kw):
		return obj(self, *p, **kw)


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

class Can(Object):
	width = 10
	height = 20
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	def create(self, cords):
		x,y = cords
		self.shape = self.scene.c.create_rectangle(x, y, self.width, self.height, outline="black", fill="red")
		return self.shape

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

	scene = Scene(Canvas)

	crossair = CrossAir(Canvas)
	fpscounter = FPS(Canvas)
	can = scene.make(Can)
	scene.create(can)
	def callback(e):
		scene.cam.x_rot = (360/500) * e.x
		crossair.update(e)
	Window.bind('<Motion>', callback)

	Canvas.pack()

	def loop(delta):
		fps = int(1/delta)
		crossair.draw()
		fpscounter.fps = fps
		scene.draw()

	gameloop = Loop(Window, GAMEFPS, loop)
	gameloop.start()

	Window.mainloop()