#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Create the main window
root = tk.Tk()
root.title("Text to Speech Converter")

# Create and place the text entry widget
text_entry = tk.Text(root, wrap="word", width=50, height=10)
text_entry.pack(pady=10)

# Event handler for the convert button click
def on_convert_button_click():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

# Create and place the convert button
convert_button = tk.Button(root, text="Convert to Speech", command=on_convert_button_click)
convert_button.pack(pady=10)

# Start the main event loop
root.mainloop()


# In[ ]:




