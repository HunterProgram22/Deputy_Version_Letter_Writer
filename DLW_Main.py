from tkinter import Tk, E
import tkinter.ttk as ttk
from DLW_Views import AppWindow
from DLW_Tabs import aod_tab, create_tab, \
    add_template_buttons, add_template_previews
from DLW_Controller import *


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
tab. Aod_tab has its own format different from other tabs."""
aod_tab(application)

"""Create_tab returns a tuple of (tab, preview_field, recipient_fields)."""
gen_tab, gen_preview_field, gen_recipient_fields = create_tab(application,
        'General Letters')
gen_tab_template_list = [('Create Not Filed Letter', GEN_NotFiledLetter),
        ('Create No Case Letter', GEN_NoCaseLetter),
        ('Create No Forms Letter', GEN_NoFormsLetter)]
gen_tab.set_col_cursor(0)
gen_tab.set_row_cursor(12)
gen_button_list = add_template_buttons(gen_tab, gen_recipient_fields,
        gen_tab_template_list)
add_template_previews(gen_button_list, gen_preview_field)


jur_tab, jur_preview_field, jur_recipient_fields = create_tab(application,
        'Jurisdictional Letters')
jur_tab_template_list = [('Late Jur-No Delayed Appeal', JUR_LateJurLetter),
        ('Late Jur-Delayed Appeal', JUR_LateJurDelayedAppealLetter),
        ('Timely Jur-Missing Docs', JUR_TimelyJurMissingDocsLetter)]
jur_tab.set_col_cursor(0)
jur_tab.set_row_cursor(12)
jur_button_list = add_template_buttons(jur_tab, jur_recipient_fields,
        jur_tab_template_list)
add_template_previews(jur_button_list, jur_preview_field)



oa_tab = create_tab(application, 'Original Action Letters')
time_tab = create_tab(application, 'Timeliness Letters')


"""Run the application."""
root.mainloop()
