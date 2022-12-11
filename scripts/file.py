import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from .common import Common as c
import tkinter.messagebox as msg
from astropy.io import fits

class FileManager:
    def __init__(self):
        self.__dlg = None
    def evOpenFile(self, event=None):
        filename = fd.askopenfilename(title='Open a file', initialdir='~', filetypes=[('FITS files', '*.fits'), ('FITS files', '*.fit'), ('FITS files', '*.fts'), ('All files', '.*')])
        if filename != '' and filename != ():
            self.openFile(filename)
            # try:
            #     self.openFile(filename)
            #     msg.showinfo(title='Open file', message=filename)
            # except Exception as e:
            #     msg.showerror(title='File open error', message='Cannot load "' + filename +'".\nThis file doesn\'t seem FITS file.')
                # print(e)
    def openFile(self, filename: str):
        if c.hdul != None:
            c.hdul.close()
        try:
            c.hdul = fits.open(filename)
        except Exception as e:
            msg.showerror(title='File open error', message='Cannot open "' + filename + '".')
            print(e, file=sys.stderr)
            return
        c.n_hdul = len(c.hdul)
        self.__dlg = tk.Toplevel(c.root)
        self.__dlg.title('FITSeye: ' + filename)
        self.__dlg.geometry('800x300')
        self.__dlg.focus_set()
        c.data = c.hdul['EVENTS']
        n: int = len(c.data.columns.names)
        for i in range(n):
            c.lItemRange.append([c.data.columns.names[i], None, None])
        c.bOpen = True

