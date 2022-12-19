import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as msg
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from astropy.io import fits
from .file import FileManager
from .definitions import *

class FITSeye:
    def __init__(self, filename: str=''):
        self.__lFileMgr = []
        self.__root = tk.Tk()
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        self.__root.geometry('200x400')
        # self.__root.resizable()
        # self.__root.attributes()
        self.__root.title(STRSOFTNAME + '')
        try:
            self.__root.iconbitmap('')
        except:
            pass
        ttk.Label(self.__root, text=STRSOFTNAME + ' version 0.1').pack()
        btn_open = self.__makeButton('Open FITS file', self.__evOpenFile).pack()
        # btn_select = self.__makeButton('Select', self.__select.evSelect).pack()
        # btn_expt = self.__makeButton('Export').pack()
        btn_about = ttk.Button(self.__root, text='About FITSeye')
        btn_about.pack()
        if filename != '':
            self.__openFile(filename)
    def __del__(self):
        pass
    def main(self):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        finally:
            self.__root.mainloop()
    def __evOpenFile(self, event):
        filename = fd.askopenfilename(title='Open a file', initialdir='~', filetypes=[('FITS files', '*.fits'), ('FITS files', '*.fit'), ('FITS files', '*.fts'), ('All files', '.*')])
        if filename != '' and filename != ():
            self.__openFile(filename)
    def __openFile(self, filename: str):
        try:
            self.__lFileMgr.append(FileManager(filename))
        except Exception as e:
            # del self.__lFileMgr[-1]
            msg.showerror(title='File open error', message='Cannot open "' + filename + '".')
            print(e, file=sys.stderr)
    # Histogram
    def __dialogHist(self, event):
        if c.__hdul != None:
            dlg = tk.Toplevel()
            dlg.title('Plot histogram')
            dlg.geometry('400x400')
            dlg.focus_set()
            btn_make = ttk.Button(dlg, text='Make', command=lambda: self.__makeHist(cmb_item_var.get()))
            # btn_make.bind('<Button-1>', lambda: self.__makeHist(x=cmb_item_var.get()))
            btn_make.grid(column=0, row=3)
            btn_close = self.__makeButton('Close', root=dlg).grid(column=1, row=3)
    # Utilities
    def __makeButton(self, text, bindFunc=None, root=None):
        if root == None:
            root = self.__root
        btn = ttk.Button(root, text=text)
        btn.bind('<Button-1>', bindFunc)
        return btn


