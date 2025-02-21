# Tkinter

import tkinter

import tkinter as tk

# Window
root = tk.Tk()
root.title("GUI")

# Label
label = tk.Label(root, text="Label:")
label.pack()

# Entry
entry = tk.Entry(root)
entry.pack()

# Handler
def on_button_click():
  print(f'entered: {entry.get()}')

# Button
button = tk.Button(root, text="Button", command=on_button_click)
button.pack()

# Event Loop
root.mainloop()