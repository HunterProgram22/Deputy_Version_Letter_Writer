from tkinter import Tk, E
import tkinter.ttk as ttk
from DLW_Views import AppWindow
from DLW_Tabs import aod_tab, create_tab, add_gen_tab_buttons, add_jur_tab_buttons


def add_weight(widget):
    """Add weight to widget so that all aspects of the widget
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
of the tkinter Frame widget. TAB_DICT is in DLW_VIEWS and provides name
and order of tabs."""
application = AppWindow(root)


"""For each tab on the application widget create the content of that
tab."""
aod_tab(application)
gen_tab = create_tab(application, 'General Letters')
add_gen_tab_buttons(gen_tab[0], gen_tab[1], gen_tab[2])
jur_tab = create_tab(application, 'Jurisdictional Letters')
add_jur_tab_buttons(jur_tab[0], jur_tab[1], jur_tab[2])
oa_tab = create_tab(application, 'Original Action Letters')
time_tab = create_tab(application, 'Timeliness Letters')


"""Run the application."""
root.mainloop()
