from index import Loop
from tkinter import Tk
import sys

root = Tk()

fps = 'unlimited'

def gameLoop(delta):
	print(int(1 / delta), end="\r")

loop = Loop(root, fps, gameLoop)

loop.start()

root.mainloop()
