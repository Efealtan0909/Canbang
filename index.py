from time import time, sleep
import tkinter as tk
from functools import partial, wraps

FPS = 60

class Loop:
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
			delta = 1
		time_delay = 0
		def loop():
			nonlocal delta
			nonlocal time_delay
			if (not self.running): pass
			exec_time = time()
			self.loop_func(delta)
			delta = time() - time_delay
			time_delay = time()
			self.schedule(exec_time, loop)
		self.schedule(0, loop)
	def stop(self):
		if (not self.running): pass
		self.running = False

# class CrossAir:
# 	def __init__(self, c):
# 		self.c = c
# 		self.x = 0
# 		self.y = 0
# 		self.shape = self.c.create_rectangle(self.x, self.y, 10, 10, outline="black", fill="white")
# 	def draw(self):
# 		self.c.move(self.shape, self.x, self.y)

# class FPS:
# 	def __init__(self, c):
# 		self

# if __name__ == "__main__":
# 	Window = tk.Tk()
# 	Window.title('Canbang')

# 	Canvas = tk.Canvas(
# 		Window,
# 		width=500,
# 		height=500,
# 		cursor="none",
# 		bg="lightblue"
# 	)

# 	crossair = CrossAir(Canvas)

# 	Canvas.pack()

# 	def loop:
# 		exec_time = time()
		

# 	Window.mainloop()