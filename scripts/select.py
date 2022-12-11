import tkinter as tk
from tkinter import ttk
from .common import Common as c

class Select:
    def __init__(self):
        self.__n: int = 0
        self.__lbls = []
        self.__dlg = None
    def evSelect(self, event):
        if c.bOpen:
            self.__dlg = tk.Toplevel()
            self.__dlg.title('Select')
            self.__dlg.geometry('500x500')
            self.__dlg.focus_set()
            # self.__dlg.columnconfigure(index=0, weight=1)
            # self.__dlg.columnconfigure(index=1, weight=2)
            # self.__dlg.columnconfigure(index=2, weight=1)
            self.__n = len(c.data.columns.names)
            # lbls_names = list(n)
            ttk.Label(self.__dlg, text='Minimum').grid(column=0, row=0)
            ttk.Label(self.__dlg, text='Item').grid(column=1, row=0)
            ttk.Label(self.__dlg, text='Maximum').grid(column=2, row=0)
            self.__lbls = []
            for i in range(self.__n):
                self.__lbls.append(ttk.Entry(self.__dlg))
                self.__lbls[2 * i].grid(column=0, row=i+1)
                ttk.Label(self.__dlg, text=c.data.columns.names[i]).grid(column=1, row=i+1)
                self.__lbls.append(ttk.Entry(self.__dlg))
                self.__lbls[2 * i + 1].grid(column=2, row=i+1)
            btn_sel = ttk.Button(self.__dlg, text='Select')
            btn_sel.bind('<Button-1>', self.__selected)
            btn_sel.grid(column=0, row=self.__n+1, pady=10)
            btn_ccl = ttk.Button(self.__dlg, text='Cancel')
            btn_ccl.bind('<Button-1>', self.__close)
            btn_ccl.grid(column=2, row=self.__n+1, pady=10)
    def __selected(self, event):
        for i in range(self.__n):
            try:
                c.lItemRange[i][1] = float(self.__lbls[2 * i].get())
            except:
                c.lItemRange[i][1] = None
            try:
                c.lItemRange[i][2] = float(self.__lbls[2 * i + 1].get())
            except:
                c.lItemRange[i][2] = None
        self.__dlg.destroy()
        # print(c.lItemRange)
    def __close(self, event):
        self.__dlg.destroy()
            
