#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tk


# In[2]:


import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Initialize the main application window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Create a Text widget
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu with commands
def new_file():
    if messagebox.askokcancel("New File", "Do you want to save the current file?"):
        save_file()
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Simple Text Editor")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{os.path.basename(file_path)} - Simple Text Editor")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{os.path.basename(file_path)} - Simple Text Editor")

def exit_editor():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu with commands
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
def show_about():
    messagebox.showinfo("About", "Simple Text Editor in Python using Tkinter")

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Run the application
root.mainloop()


# In[ ]:




