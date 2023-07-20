
import tkinter as tk
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file is not None:
        text_editor.delete('1.0', tk.END)
        text_editor.insert(tk.END, file.read())

def save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file is not None:
        file.write(text_editor.get('1.0', tk.END))
        file.close()

def exit_editor():
    window.destroy()

window = tk.Tk()
window.title("Text Editor")

text_editor = tk.Text(window)
text_editor.pack()

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()