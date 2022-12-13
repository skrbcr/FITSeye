import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as msg
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from astropy.io import fits
from .common import Common as c
from .file import FileManager
from .select import Select

class FITSeye:
    def __init__(self, filename: str=''):
        self.__lFileMgr = []
        self.__root = tk.Tk()
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        self.__root.geometry('600x400')
        # self.__root.resizable()
        # self.__root.attributes()
        self.__root.title('FITSeye')
        try:
            self.__root.iconbitmap('')
        except:
            pass
        ttk.Label(self.__root, text='FITSeye version 0.1').pack()
        btn_open = self.__makeButton('Open FITS file', self.__evOpenFile).pack()
        # btn_select = self.__makeButton('Select', self.__select.evSelect).pack()
        # btn_hist = self.__makeButton('Histogram', self.__dialogHist).pack()
        # btn_plot = self.__makeButton('2D Plot', self.__dialog2d).pack()
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
            # dlg.columnconfigure(0, 1)
            # dlg.columnconfigure(1, 1)
            # dlg.rowconfigure
            lbl_max = ttk.Label(dlg, text='Max: ').grid(column=0, row=1)
            lbl_max_num = ttk.Label(dlg)
            lbl_max_num.grid(column=1, row=1)
            lbl_min = ttk.Label(dlg, text='Min: ').grid(column=0, row=2)
            lbl_min_num = ttk.Label(dlg)
            lbl_min_num.grid(column=1, row=2)
            def data(event):
                value = cmb_item_var.get()
                lbl_max_num['text'] = str(np.max(c.data[value]))
                lbl_min_num['text'] = str(np.min(c.data[value]))
            cmb_item_var = tk.StringVar()
            cmb_item = ttk.Combobox(dlg, textvariable=cmb_item_var, values=c.data.columns.names)
            cmb_item.bind('<<ComboboxSelected>>', data)
            cmb_item.grid(column=0, row=0, columnspan=1)
            btn_make = ttk.Button(dlg, text='Make', command=lambda: self.__makeHist(cmb_item_var.get()))
            # btn_make.bind('<Button-1>', lambda: self.__makeHist(x=cmb_item_var.get()))
            btn_make.grid(column=0, row=3)
            btn_close = self.__makeButton('Close', root=dlg).grid(column=1, row=3)
    def __makeHist(self, x=None):
        if x != None:
            fig, ax = plt.subplots()
            ax.grid()
            ax.hist(c.data[x], color='r', histtype='step')
            plt.show()
    # 2D Histogram
    def __dialog2d(self, event):
        if c.__hdul != None:
            fig, ax = plt.subplots()
            arrx = c.data.x
            arry = c.data.y
            ax.hist2d(arrx, arry)
            plt.show()
    # Utilities
    def __makeButton(self, text, bindFunc=None, root=None):
        if root == None:
            root = self.__root
        btn = ttk.Button(root, text=text)
        btn.bind('<Button-1>', bindFunc)
        return btn


