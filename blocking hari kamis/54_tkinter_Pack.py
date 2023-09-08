import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="Label1")
label.pack()

button = tk.Button(root, text="Tombol1")
button.pack()

checkbox=tk.Checkbutton(root, text="Centang1")
checkbox.pack()
root.mainloop()

