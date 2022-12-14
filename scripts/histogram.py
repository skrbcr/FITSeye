import sys
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
from astropy.io import fits
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px

mpl.style.use('fast')

class Hist:
    def __init__(self, master, hdu):
        self.__hdu = hdu
        self.__lcolname = ['--None--'] + hdu.columns.names
        self.__cmbField = [None, None]
        self.__lblField = [[None, None, None, None], [None, None, None, None]]
        self.__etrField = [[None, None, None], [None, None, None]]
        self.__btn = [None, None, None]
        self.__makeTopDlg(master)
        self.__strNone = '--None--'
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
        ttk.Label(self.__dlgTop, text='Bin Size').grid(row=9, column=0)
        self.__etrField[0][2] = ttk.Entry(self.__dlgTop)
        self.__etrField[0][2].grid(row=9, column=1)
        self.__etrField[1][2] = ttk.Entry(self.__dlgTop)
        self.__etrField[1][2].grid(row=9, column=2)
        for i in range(2):
            self.__cmbField[i] = ttk.Combobox(self.__dlgTop, values=self.__lcolname)
            self.__cmbField[i].bind('<<ComboboxSelected>>', lambda event, axis=i: self.__makeField(axis))
            self.__cmbField[i].grid(row=2, column=i+1)
        self.__btn[0] = ttk.Button(self.__dlgTop, text='Make', command=self.__makeHist)
        self.__btn[0].grid(row=10, column=0)
        self.__btn[1] = ttk.Button(self.__dlgTop, text='Export')#, command=self.__makeHist)
        self.__btn[1].grid(row=10, column=1)
        self.__btn[2] = ttk.Button(self.__dlgTop, text='Close', command=self.__dlgTop.destroy)
        self.__btn[2].grid(row=10, column=2)
    def __makeField(self, axis: int):
        value = self.__cmbField[axis].get()
        bLim = True
        if value == self.__strNone:
            self.__lblField[axis][0]['text'] = '---'
            self.__lblField[axis][1]['text'] = '---'
            self.__lblField[axis][2]['text'] = '---'
            self.__lblField[axis][3]['text'] = '---'
            self.__etrField[axis][0].delete(0, tk.END)
            self.__etrField[axis][1].delete(0, tk.END)
            self.__etrField[axis][2].delete(0, tk.END)
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
            self.__etrField[axis][0].delete(0, tk.END)
            self.__etrField[axis][1].delete(0, tk.END)
            self.__etrField[axis][2].delete(0, tk.END)
            if bLim:
                self.__etrField[axis][0].insert(tk.END, str(self.__lblField[axis][0]['text']))
                self.__etrField[axis][1].insert(tk.END, str(self.__lblField[axis][1]['text']))
                if 'i' in str(self.__hdu.data[value].dtype) or 'u' in str(self.__hdu.data[value].dtype):
                    __bin = np.ceil(np.power(2., np.ceil(np.log2((float(self.__lblField[axis][0]['text']) - float(self.__lblField[axis][1]['text'])) / 500.))))
                elif 'f' in str(self.__hdu.data[value].dtype):
                    __bin = np.power(2., np.ceil(np.log2((float(self.__lblField[axis][0]['text']) - float(self.__lblField[axis][1]['text'])) / 500.)))
                else:
                    __bin = ''
            else:
                self.__etrField[axis][0].insert(tk.END, str(self.__lblField[axis][2]['text']))
                self.__etrField[axis][1].insert(tk.END, str(self.__lblField[axis][3]['text']))
                if 'i' in str(self.__hdu.data[value].dtype) or 'u' in str(self.__hdu.data[value].dtype):
                    __bin = np.ceil(np.power(2., np.ceil(np.log2((float(self.__lblField[axis][2]['text']) - float(self.__lblField[axis][3]['text'])) / 500.))))
                elif 'f' in str(self.__hdu.data[value].dtype):
                    __bin = np.power(2., np.ceil(np.log2((float(self.__lblField[axis][2]['text']) - float(self.__lblField[axis][3]['text'])) / 500.)))
                else:
                    __bin = ''
            self.__etrField[axis][2].insert(tk.END, str(__bin))
    def __makeHist(self):
        xvalue = self.__cmbField[0].get()
        yvalue = self.__cmbField[1].get()
        nHistDim = 2
        # Check Inputs
        if xvalue in self.__lcolname:
            if xvalue == self.__strNone or xvalue == '':
                msg.showerror(title='Data select error', message='Please select x axis data')
                return
            else:
                ix = self.__lcolname.index(xvalue)
        else:
            msg.showerror(title='Data select error', message='Please select proper x data.\nItem "' + xvalue + '" does not exist.')
            return
        if yvalue in self.__lcolname or yvalue == '':
            if yvalue == self.__strNone or yvalue == '':
                nHistDim = 1
            else:
                iy = self.__lcolname.index(yvalue)
        else:
            msg.showerror(title='Data select error', message='Please select proper y data.\nItem "' + yvalue + '" does not exist.')
            return
        # Draw Graph
        try:
            xmax = float(self.__etrField[0][0].get())
        except:
            try:
                xmax = float(self.__lblField[0][0]['text'])
            except:
                try:
                    xmax = float(self.__lblField[0][2]['text'])
                except:
                    msg.showerror(title='Input number error', message='Please specify Max of X properly')
        try:
            xmin = float(self.__etrField[0][1].get())
            if xmin > xmax:
                xmin, xmax = xmax, xmin
        except:
            try:
                xmin = float(self.__lblField[0][1]['text'])
            except:
                try:
                    xmin = float(self.__lblField[0][3]['text'])
                except:
                    msg.showerror(title='Input number error', message='Please specify Min of X properly')
        try:
            __xbinsize = float(self.__etrField[0][2].get())
            xbin = int((xmax - xmin) / __xbinsize)
        except:
            msg.showerror(title='Input number error', message='Please specify Bin Size of X properly')
            return
        try:
            xunit = ' / ' + self.__hdu.header['TUNIT' + str(ix)]
        except:
            xunit = ''
        if nHistDim == 1:
            lx = np.array(self.__hdu.data[xvalue], dtype=float)
            x = np.linspace(xmin, xmax, xbin)
            hist, _ = np.histogram(lx, bins=xbin, range=(xmin, xmax))
            fig, ax = plt.subplots()
            ax.plot(x, hist)
            ax.grid()
            ax.set_xlabel(xvalue + xunit)
            ax.set_ylabel('counts')
            plt.show()
            plt.clf()
            plt.close()
        else:
            try:
                ymax = float(self.__etrField[1][0].get())
            except:
                try:
                    ymax = float(self.__lblField[1][0]['text'])
                except:
                    try:
                        ymax = float(self.__lblField[1][2]['text'])
                    except:
                        msg.showerror(title='Input number error', message='Please specify Max of Y properly')
            try:
                ymin = float(self.__etrField[1][1].get())
                if ymin > ymax:
                    ymin, ymax = ymax, ymin
            except:
                try:
                    ymin = float(self.__lblField[1][1]['text'])
                except:
                    try:
                        ymin = float(self.__lblField[1][3]['text'])
                    except:
                        msg.showerror(title='Input number error', message='Please specify Min of Y properly')
            try:
                __ybinsize = float(self.__etrField[1][2].get())
                ybin = int((ymax - ymin) / __ybinsize)
            except:
                msg.showerror(title='Input number error', message='Please specify Bin Size of Y properly')
                return
            try:
                yunit = ' / ' + self.__hdu.header['TUNIT' + str(iy)]
            except:
                yunit = ''
            lx = np.array(self.__hdu.data[xvalue], dtype=float)
            ly = np.array(self.__hdu.data[yvalue], dtype=float)
            # n = len(self.__hdu.data[xvalue])
            # for i in range(n):
            #     if xmin <= self.__hdu.data[xvalue][i] and self.__hdu.data[xvalue][i] <= xmax and ymin <= self.__hdu.data[yvalue][i] and self.__hdu.data[yvalue][i] <= ymax
            #         lx.append(self.__hdu.data[xvalue][i])
            #         ly.append(self.__hdu.data[yvalue][i])
            fig, ax = plt.subplots()
            ax.set_aspect('equal')
            hi, xe, ye, img = ax.hist2d(lx, ly, bins=[xbin, ybin], range=[[xmin, xmax], [ymin, ymax]])
            ax.set_xlabel(xvalue + xunit)
            ax.set_ylabel(yvalue + yunit)
            plt.colorbar(img)
            plt.show()
            plt.clf()
            plt.close()

