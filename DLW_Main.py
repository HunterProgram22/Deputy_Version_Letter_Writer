from tkinter import Tk, E
import tkinter.ttk as ttk
from DLW_Views import AppWindow, create_aod_tab, create_tab, add_template_buttons, \
    add_template_previews, populate_tab_content, add_weight
from DLW_Models import *

TAB_DICT = {'General Letters': 0, 'Jurisdictionals': 1,
        'Direct Appeals': 2, 'Delayed Appeals': 3,
        'Original Actions': 4, 'Briefs and Motions': 5,
        'Amended Docs': 6, 'AOD Letters': 7}

GEN_TAB_TEMPLATE_LIST = [('Document Not Filed', GEN_NotFiledLetter),
        ('No Case Pending', GEN_NoCaseLetter),
        ('No Forms', GEN_NoFormsLetter),
        ('Blank Letter', GEN_BlankLetter)]
JUR_TAB_TEMPLATE_LIST = [('Late-No Delayed Appeal', JUR_LateJurLetter),
        ('Late-Delayed Appeal', JUR_LateJurDelayedAppealLetter),
        ('No Extension-Delayed App.', JUR_NoExtensionLetter),
        ('Timely-Missing Docs', JUR_TimelyJurMissingDocsLetter)]
DAF_TAB_TEMPLATE_LIST = [('Missing Opinion', DAF_NoOpinionLetter),
        ('No Facts Aff.', DAF_NoFactsAffLetter),
        ('Delayed App. Not Allowed', DAF_NotAllowedLetter)]
OA_TAB_TEMPLATE_LIST = [('No Respondent Address', OA_NoAddressLetter),
        ('No Aff In Support', OA_NotNotarizedLetter),
        ('No Security Deposit', OA_NoSecurityDepositLetter),
        ('No Address/AFF/SecDep', OA_NoAddNoSecDepNoAffLetter)]
DAP_TAB_TEMPLATE_LIST = [('Premature Brief', DAP_PrematureBriefLetter)]
TIMELY_TAB_TEMPLATE_LIST = [('Late Merit Brief', LateBriefLetter),
        ('No Recon Allowed', NoReconLetter),
        ('Late Recon', LateReconLetter)]
AMEND_TAB_TEMPLATE_LIST = [('Amend Jur Memo', AmendJurLetter),
        ('Late Amended Jur Memo', LateAmendedJurLetter)]

root = Tk()
root.geometry("1050x900")
root.title("General Letter Writer")
add_weight(root)
application = AppWindow(root, TAB_DICT)

"""Aod_tab has its own format different from other tabs and uses a specific
function for creation."""
create_aod_tab(application)

populate_tab_content(application, 'General Letters', GEN_TAB_TEMPLATE_LIST)
populate_tab_content(application, 'Jurisdictionals', JUR_TAB_TEMPLATE_LIST)
populate_tab_content(application, 'Delayed Appeals', DAF_TAB_TEMPLATE_LIST)
populate_tab_content(application, 'Original Actions', OA_TAB_TEMPLATE_LIST)
populate_tab_content(application, 'Direct Appeals', DAP_TAB_TEMPLATE_LIST)
populate_tab_content(application, 'Briefs and Motions', TIMELY_TAB_TEMPLATE_LIST)
populate_tab_content(application, 'Amended Docs', AMEND_TAB_TEMPLATE_LIST)

root.mainloop()
