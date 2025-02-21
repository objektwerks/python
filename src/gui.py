# Tkinter

import tkinter as tk
from tkinter import Button, Entry, Label, Tk

# Window
window: Tk = tk.Tk()
window.title("GUI")
window.eval('tk::PlaceWindow . center')

# Label
label: Label = tk.Label(window, text="Label:")
label.pack()

# Entry
entry: Entry = tk.Entry(window)
entry.pack()

# Handler
def on_button_click():
  print(f'text entered: {entry.get()}')

# Button
button: Button = tk.Button(
  window,
  text="Button",
  command=on_button_click
)
button.pack()

# Event Loop
window.mainloop()