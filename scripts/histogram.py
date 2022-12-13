import sys
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
from astropy.io import fits
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class Hist:
    def __init__(self, master, hdu):
        self.__hdu = hdu
        self.__lcolname = ['--None--'] + hdu.columns.names
        self.__cmbField = [None, None]
        self.__lblField = [[None, None, None, None], [None, None, None, None]]
        self.__etrField = [[None, None, None], [None, None, None]]
        self.__makeTopDlg(master)
    def __makeTopDlg(self, master):
        self.__dlgTop = tk.Toplevel(master)
        self.__dlgTop.title('FITSeye: Histogram')
        self.__dlgTop.geometry('600x400')
        self.__dlgTop.focus_set()
        ttk.Label(self.__dlgTop, text='Histogram (1D or 2D)').grid(row=0, column=0)
        ttk.Label(self.__dlgTop, text='X').grid(row=1, column=1)
        ttk.Label(self.__dlgTop, text='Y').grid(row=1, column=2)
        ttk.Label(self.__dlgTop, text='Column Name').grid(row=2, column=0)
        ttk.Label(self.__dlgTop, text='Limit Max (TLMax)').grid(row=3, column=0)
        self.__lblField[0][0] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[0][0].grid(row=3, column=1)
        self.__lblField[1][0] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[1][0].grid(row=3, column=2)
        ttk.Label(self.__dlgTop, text='Limit Min (TLMin)').grid(row=4, column=0)
        self.__lblField[0][1] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[0][1].grid(row=4, column=1)
        self.__lblField[1][1] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[1][1].grid(row=4, column=2)
        ttk.Label(self.__dlgTop, text='Data Max').grid(row=5, column=0)
        self.__lblField[0][2] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[0][2].grid(row=5, column=1)
        self.__lblField[1][2] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[1][2].grid(row=5, column=2)
        ttk.Label(self.__dlgTop, text='Data Min').grid(row=6, column=0)
        self.__lblField[0][3] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[0][3].grid(row=6, column=1)
        self.__lblField[1][3] = ttk.Label(self.__dlgTop, text='---')
        self.__lblField[1][3].grid(row=6, column=2)
        ttk.Label(self.__dlgTop, text='Max').grid(row=7, column=0)
        self.__etrField[0][0] = ttk.Entry(self.__dlgTop)
        self.__etrField[0][0].grid(row=7, column=1)
        self.__etrField[1][0] = ttk.Entry(self.__dlgTop)
        self.__etrField[1][0].grid(row=7, column=2)
        ttk.Label(self.__dlgTop, text='Min').grid(row=8, column=0)
        self.__etrField[0][1] = ttk.Entry(self.__dlgTop)
        self.__etrField[0][1].grid(row=8, column=1)
        self.__etrField[1][1] = ttk.Entry(self.__dlgTop)
        self.__etrField[1][1].grid(row=8, column=2)
        ttk.Label(self.__dlgTop, text='Bins').grid(row=9, column=0)
        self.__etrField[0][2] = ttk.Entry(self.__dlgTop)
        self.__etrField[0][2].grid(row=9, column=1)
        self.__etrField[1][2] = ttk.Entry(self.__dlgTop)
        self.__etrField[1][2].grid(row=9, column=2)
        for i in range(2):
            self.__cmbField[i] = ttk.Combobox(self.__dlgTop, values=self.__lcolname)
            self.__cmbField[i].bind('<<ComboboxSelected>>', lambda event, axis=i: self.__makeField(axis))
            self.__cmbField[i].grid(row=2, column=i+1)
    def __makeField(self, axis: int):
        value = self.__cmbField[axis].get()
        bLim = True
        if value == '--None--':
            self.__lblField[axis][0]['text'] = '---'
            self.__lblField[axis][1]['text'] = '---'
            self.__lblField[axis][2]['text'] = '---'
            self.__lblField[axis][3]['text'] = '---'
        else:
            try:
                self.__lblField[axis][0]['text'] = str(self.__hdu.header['TLMAX' + str(self.__lcolname.index(value))])
            except:
                try:
                    self.__lblField[axis][0]['text'] = str(self.__hdu.header['TDMAX' + str(self.__lcolname.index(value))])
                except:
                    self.__lblField[axis][0]['text'] = '---'
                    bLim = False
            try:
                self.__lblField[axis][1]['text'] = str(self.__hdu.header['TLMIN' + str(self.__lcolname.index(value))])
            except:
                try:
                    self.__lblField[axis][1]['text'] = str(self.__hdu.header['TDMIN' + str(self.__lcolname.index(value))])
                except:
                    self.__lblField[axis][1]['text'] = '---'
                    bLim = False
            self.__lblField[axis][2]['text'] = np.max(self.__hdu.data[value])
            self.__lblField[axis][3]['text'] = np.min(self.__hdu.data[value])
            if bLim:
                pass
                # self.__etrField[axis][0]['text'] = self.__lblField[axis][0]['text']
                # self.__etrField[axis][1]['text'] = self.__lblField[axis][1]['text']
            else:
                pass

