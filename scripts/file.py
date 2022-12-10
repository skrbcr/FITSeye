import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd

def openfile(event):
    filename = fd.askopenfilename(title='Open a file', initialdir='~', filetypes=[('FITS files', '*.fits'), ('FITS files', '*.fit'), ('FITS files', '*.fts'), ('All files', '.*')])
    print(filename)
    if filename != '' and filename != ():
        showinfo(title='Open file', message=filename)
    else:
        filename = None
    return filename
