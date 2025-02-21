# Tkinter

import tkinter as tk
from tkinter import Button, Entry, Label, Tk

# Window
window: Tk = tk.Tk()
window.title("GUI")
window.eval('tk::PlaceWindow . center')

# Label
label: Label = tk.Label(window, text="Label:")
label.pack(padx=5, pady=15, side=tk.LEFT)

# Entry
entry: Entry = tk.Entry(window)
entry.pack(padx=5, pady=20, side=tk.LEFT)

# Handler
def on_button_click():
  print(f'text entered: {entry.get()}')

# Button
button: Button = tk.Button(
  window,
  text="Button",
  command=on_button_click
)
button.pack(padx=5, pady=20, side=tk.LEFT)

# Event Loop
window.mainloop()