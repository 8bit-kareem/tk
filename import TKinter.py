import tkinter as tk
window = tk.Tk()
label = tk.Label(
    text="press the button",
    foreground = "black",
    background = "yellow",
    padx=100,
    pady=100
)
label.pack()
button = tk.Button(
    text="Click me",
    background = "cyan")
button.pack()
label = tk.Label(
    text="what is your name",
    background = "purple",
    padx=100,
    pady=100
    )
entry = tk.Entry()
label.pack()
entry.pack()
window.mainloop()
