from tkinter import Tk, E
import tkinter.ttk as ttk
from DLW_Views import AppWindow, create_aod_tab, create_tab, add_template_buttons, \
    add_template_previews
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

"""The values for the TAB_DICT are currently irrelevant. Could put tab
names in place of numbers if there is need to use elsewhere."""
TAB_DICT = {'General Letters': 0, 'Jurisdictionals': 1,
        'Direct Appeals': 2, 'Delayed Appeals': 3,
        'Original Actions': 4, 'Briefs and Motions': 5,
        'Amended Docs': 6, 'AOD Letters': 7}
application = AppWindow(root, TAB_DICT)



"""Aod_tab has its own format different from other tabs and uses a specific
function for creation."""
create_aod_tab(application)

"""Create_tab returns a tuple of (tab, preview_field, recipient_fields)."""
gen_tab, gen_preview_field, gen_recipient_fields = create_tab(application,
        'General Letters')
gen_tab_template_list = [('Document Not Filed', GEN_NotFiledLetter),
        ('No Case Pending', GEN_NoCaseLetter),
        ('No Forms', GEN_NoFormsLetter),
        ('Blank Letter', GEN_BlankLetter)]
gen_tab.set_col_cursor(0)
gen_tab.set_row_cursor(12)
gen_button_list = add_template_buttons(gen_tab, gen_recipient_fields,
        gen_tab_template_list)
add_template_previews(gen_button_list, gen_preview_field)

jur_tab, jur_preview_field, jur_recipient_fields = create_tab(application,
        'Jurisdictionals')
jur_tab_template_list = [('Late-No Delayed Appeal', JUR_LateJurLetter),
        ('Late-Delayed Appeal', JUR_LateJurDelayedAppealLetter),
        ('No Extension-Delayed App.', JUR_NoExtensionLetter),
        ('Timely-Missing Docs', JUR_TimelyJurMissingDocsLetter)]
jur_tab.set_col_cursor(0)
jur_tab.set_row_cursor(12)
jur_button_list = add_template_buttons(jur_tab, jur_recipient_fields,
        jur_tab_template_list)
add_template_previews(jur_button_list, jur_preview_field)

daf_tab, daf_preview_field, daf_recipient_fields = create_tab(application,
        'Delayed Appeals')
daf_tab_template_list = [('Missing Opinion', DAF_NoOpinionLetter),
        ('No Facts Aff.', DAF_NoFactsAffLetter),
        ('Delayed App. Not Allowed', DAF_NotAllowedLetter)]
daf_tab.set_col_cursor(0)
daf_tab.set_row_cursor(12)
daf_button_list = add_template_buttons(daf_tab, daf_recipient_fields,
        daf_tab_template_list)
add_template_previews(daf_button_list, daf_preview_field)

oa_tab, oa_preview_field, oa_recipient_fields = create_tab(application,
        'Original Actions')
oa_tab_template_list = [('No Respondent Address', OA_NoAddressLetter),
        ('No Aff In Support', OA_NotNotarizedLetter),
        ('No Security Deposit', OA_NoSecurityDepositLetter),
        ('No Address/AFF/SecDep', OA_NoAddNoSecDepNoAffLetter)
        ]
oa_tab.set_col_cursor(0)
oa_tab.set_row_cursor(12)
oa_button_list = add_template_buttons(oa_tab, oa_recipient_fields,
        oa_tab_template_list)
add_template_previews(oa_button_list, oa_preview_field)

dap_tab, dap_preview_field, dap_recipient_fields = create_tab(application,
        'Direct Appeals')
dap_tab_template_list = [('Premature Brief', DAP_PrematureBriefLetter),
        ]
dap_tab.set_col_cursor(0)
dap_tab.set_row_cursor(12)
dap_button_list = add_template_buttons(dap_tab, dap_recipient_fields,
        dap_tab_template_list)
add_template_previews(dap_button_list, dap_preview_field)

time_tab, time_preview_field, time_recipient_fields = create_tab(application,
        'Briefs and Motions')
time_tab_template_list = [('Late Merit Brief', LateBriefLetter),
        ('No Recon Allowed', NoReconLetter),
        ('Late Recon', LateReconLetter),
        ]
time_tab.set_col_cursor(0)
time_tab.set_row_cursor(12)
time_button_list = add_template_buttons(time_tab, time_recipient_fields,
        time_tab_template_list)
add_template_previews(time_button_list, time_preview_field)

amend_tab, amend_preview_field, amend_recipient_fields = create_tab(application,
        'Amended Docs')
amend_tab_template_list = [('Amend Jur Memo', AmendJurLetter),
        ('Late Amended Jur Memo', LateAmendedJurLetter),
        ]
amend_tab.set_col_cursor(0)
amend_tab.set_row_cursor(12)
amend_button_list = add_template_buttons(amend_tab, amend_recipient_fields,
        amend_tab_template_list)
add_template_previews(amend_button_list, amend_preview_field)


"""Run the application."""
root.mainloop()
