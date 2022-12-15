import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as msg
from astropy.io import fits
from .histogram import Hist

class FileManager:
    def __init__(self, filename: str):
        # Read FITS file
        self.__filename = filename
        try:
            self.__hdul = fits.open(filename)
        except Exception as e:
            self.__hdul = None
            raise e
        # Analyze HDUL
        self.__lenHDUL: int = len(self.__hdul)
        # Make File Top Dialog
        try:
            self.__makeTopDlg()
        except Exception as e:
            print('Error: something went wrong with making "File Top Dialog". Please notify the author on this issue.', file=sys.stderr)
            raise e
        self.__lhist = []
    def __del__(self):
        if self.__hdul != None:
            self.__hdul.close()
    def __makeTopDlg(self):
        # Dialog
        self.__dlgTop = tk.Toplevel()
        self.__dlgTop.title('FITSeye: Summary of ' + self.__filename)
        self.__dlgTop.geometry('800x300')
        self.__dlgTop.focus_set()
        # Table
        ttk.Label(self.__dlgTop, text='Index').grid(row=0, column=0)
        ttk.Label(self.__dlgTop, text='Extension').grid(row=0, column=1)
        ttk.Label(self.__dlgTop, text='Table Size').grid(row=0, column=2)
        for i, hdu in enumerate(self.__hdul):
            summary = hdu._summary()
            ttk.Label(self.__dlgTop, text=str(i)).grid(row=i+1, column=0)
            ttk.Label(self.__dlgTop, text=str(summary[0])).grid(row=i+1, column=1)
            ttk.Label(self.__dlgTop, text=str(summary[4])).grid(row=i+1, column=2)
            # Buttons
            if hdu.header['NAXIS'] == 0:
                ttk.Button(self.__dlgTop, text='Header').grid(row=i+1, column=3)
            else:
                btn = ttk.Button(self.__dlgTop, text='Hist')
                btn.bind('<Button-1>', lambda event, i=i: self.__hist(i))
                ttk.Button(self.__dlgTop, text='Header').grid(row=i+1, column=3)
                btn.grid(row=i+1, column=4)
                ttk.Button(self.__dlgTop, text='Table').grid(row=i+1, column=5)
        # Menu
        menubar = tk.Menu(self.__dlgTop)
        self.__dlgTop.config(menu=menubar)
        menu_file = tk.Menu(menubar, tearoff=False)
        menu_file.add_command(label='Export(not available now)')
        menu_file.add_separator()
        menu_file.add_command(label='Quit', command=self.__dlgTop.destroy)
        menubar.add_cascade(label='File', menu=menu_file, underline=0)
    def __hist(self, i: int):
        self.__lhist.append(Hist(self.__dlgTop, self.__hdul[i]))

