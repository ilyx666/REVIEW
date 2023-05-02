import tkinter as tk
from tkinter import Text

def button_click():
    value1 = entry1.get()
    value2 = entry2.get("1.0", "end-1c")
    print("Количество фото:", value1)
    print("Отзыв:", value2)

root = tk.Tk()
root.geometry("900x600")

label1 = tk.Label(root, text="Количество фото:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Отзыв:")
label2.pack()

entry2 = tk.Text(root, width=50, height=10)
entry2.pack()

button = tk.Button(root, text="ГОТОВО!", command=button_click)
button.pack()

root.mainloop()
