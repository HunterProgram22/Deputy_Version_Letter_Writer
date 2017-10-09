from tkinter import Tk, E
import tkinter.ttk as ttk
from DLW_Views import AppWindow
#from DLW_Controller import *
from DLW_Tabs import aod_tab, gen_tab


def add_weight(widget):
    """Add weight to a tkinter widget so that all aspects of the widget
    are visible without scrolling."""
    rows = 0
    while rows < 50:
        widget.rowconfigure(rows, weight=1)
        widget.columnconfigure(rows, weight=1)
        rows += 1
    return None


"""Create the main tkinter widget that is the base on which all
other widgets will be rooted."""
root = Tk()
root.geometry("1050x900")
root.title("General Letter Writer")
add_weight(root)


"""Create the main application widget that is placed on the root widget.
This application is an instance of a AppWindow class that is a subclass
of the tkinter Frame widget. The list of tabs is currently a constant in
DLW_Views."""
application = AppWindow(root)


"""For each tab on the application widget create the content of that
tab."""
aod_tab(application)
gen_tab(application)


"""Run the application."""
root.mainloop()
