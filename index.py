import tkinter as tk

Window = tk.Tk()
Window.title('Canbang')

Button = tk.Button(
    text="Click to Start the Game",
    command="StartGame",
    width=25,
    height=5,
    bg="green",
    fg="white",
)

Button.pack()

Window.mainloop()