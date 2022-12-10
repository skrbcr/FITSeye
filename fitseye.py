import tkinter as tk
from tkinter import ttk
from scripts.main import winmain

def main():
    # create window
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry('600x400')
    # root.resizable()
    # root.attributes()
    root.title('FITSeye')
    try:
        root.iconbitmap('')
    except:
        pass
    # call contents
    winmain(root)
    # mainloop
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    finally:
        root.mainloop()

main()

