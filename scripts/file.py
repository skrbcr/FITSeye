import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from .common import Common as c
import tkinter.messagebox as msg
from astropy.io import fits

class FileDialog:
    def __init__(self):
        pass
    def evOpenFile(self, event):
        filename = fd.askopenfilename(title='Open a file', initialdir='~', filetypes=[('FITS files', '*.fits'), ('FITS files', '*.fit'), ('FITS files', '*.fts'), ('All files', '.*')])
        if filename != '' and filename != ():
            try:
                FileDialog.openFile(filename)
                msg.showinfo(title='Open file', message=filename)
            except Exception as e:
                msg.showerror(title='File open error', message='Cannot load "' + filename +'".\nThis file doesn\'t seem FITS file.')
                print(e)
    def openFile(filename: str):
        c.hdul = fits.open(filename)
        c.data = c.hdul['EVENTS']
        c.bOpen = True

