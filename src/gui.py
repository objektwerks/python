# Tkinter

import tkinter as tk
from tkinter import Entry, Label, Tk

# Window
root: Tk = tk.Tk()
root.title("GUI")

# Label
label: Label = tk.Label(root, text="Label:")
label.pack()

# Entry
entry: Entry = tk.Entry(root)
entry.pack()

# Handler
def on_button_click():
  print(f'text entered: {entry.get()}')

# Button
button = tk.Button(root, text="Button", command=on_button_click)
button.pack()

# Event Loop
root.mainloop()