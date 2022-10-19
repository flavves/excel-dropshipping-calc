# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:46:50 2022

@author: okmen
"""

import tkinter as tk
r = tk.Tk()
r.title('mac deneme')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()