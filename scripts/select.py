import tkinter as tk
from tkinter import ttk
from .common import Common as c

class Select:
    def __init__(self):
        pass
    def evSelect(self, event):
        if c.bOpen:
            dlg = tk.Toplevel()
            dlg.title('Select')
            dlg.geometry('400x400')
            dlg.focus_set()
            n: int = len(c.data.columns.names)
            # lbls_names = list(n)
            for i in range(n):
                ttk.Label(dlg, text=c.data.columns.names[i]).grid(column=1, row=i)
            # dlg.columnconfigure(0, 1)
            # dlg.columnconfigure(1, 1)
            # dlg.rowconfigure
     

