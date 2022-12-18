import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox as msg
from astropy.io import fits

class Table:
    def __init__(self, master, hdu, filename: str, nIndex: int):
        self.__master = master
        self.__hdu = hdu
        self.__filename = filename
        self.__nHDU = nIndex
        try:
            self.__makeTopDlg()
        except Exception as e:
            print('Error: something went wrong with making "Table Dialog". Please notify the author on this issue.', file=sys.stderr)
            raise e
    def __makeTopDlg(self):
        self.__dlgTop = tk.Toplevel(master=self.__master)
        self.__dlgTop.title('FITSeye: Table of HDU No.' + str(self.__nHDU) + ' of ' + self.__filename)
        self.__dlgTop.geometry('800x500')
        self.__tree = ttk.Treeview(self.__dlgTop, columns=['index'] + self.__hdu.columns.names, show='headings')
        self.__scrbar = ttk.Scrollbar(self.__dlgTop, orient=tk.HORIZONTAL, command=self.__tree.xview)
        self.__tree.heading('index', text='index')
        for name in self.__hdu.columns.names:
            self.__tree.heading(name, text=name)
        n = len(self.__hdu.data)
        if n < 1000:
            for i, row in enumerate(self.__hdu.data):
                self.__tree.insert('', tk.END, values=tuple([str(i + 1)] + row))
        else:
            self.__tree.insert('', tk.END, values=(1, *self.__hdu.data[0]))
            self.__tree.insert('', tk.END, values=(2, *self.__hdu.data[1]))
            self.__tree.insert('', tk.END, values=(3, *self.__hdu.data[2]))
            self.__tree.insert('', tk.END, values=(n - 2, *self.__hdu.data[n - 3]))
            self.__tree.insert('', tk.END, values=(n - 1, *self.__hdu.data[n - 2]))
            self.__tree.insert('', tk.END, values=(n, *self.__hdu.data[n - 1]))
        self.__tree.pack()
        self.__tree.configure(xscrollcommand=lambda f, l: self.__scrbar.set(f, l))
        self.__scrbar.pack(fill='x')
