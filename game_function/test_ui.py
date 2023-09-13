import tkinter as tk

root = tk.Tk()


def key_event(e):
    print(e.keysym)


root.bind("<KeyPress>", key_event)

root.mainloop()
