#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:26:50 2018

@author: gabriel
"""
import tkinter as tk
from os import get_terminal_size


def onKeyPress(event):
    os.system("clear")
    print(event.keysym)

root = tk.Tk()
text = tk.Text(root)
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
