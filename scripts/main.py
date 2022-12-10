import tkinter as tk
from tkinter import ttk
from . import file

def makeButton(root, text, bindFunc=None):
    btn = ttk.Button(root, text=text)
    btn.bind('<Button-1>', bindFunc)
    btn.pack()
    return btn

def winmain(root):
    ttk.Label(root, text='FITSeye version 0.1').pack()
    btn_open = makeButton(root, 'Open FITS file', file.openfile)
    btn_select = makeButton(root, 'Select')
    btn_hist = makeButton(root, 'Histgram')
    btn_plot = makeButton(root, '2D Plot')
    btn_expt = makeButton(root, 'Export')
