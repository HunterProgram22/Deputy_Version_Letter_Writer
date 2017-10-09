from tkinter import END
import tkinter as tk
from DLW_Models import Address, JudgeAddress, CaseInformation, \
    AttorneyAddress, AODRequirements, PrisonerAddress
from DLW_Controller import *
from DLW_Views import *
from Tool_Tips import *

class CreatePreview(object):
    """
    create preview text for the letter when hovering on button
    """
    def __init__(self, widget, destination, text='widget info'):
        self.waittime = 500     #milliseconds
        self.widget = widget
        self.destination = destination
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        self.destination.insert("1.0", self.text)

    def leave(self, event=None):
        self.destination.delete("1.0", END)


"___AOD Letters TAB___"
def aod_tab(application):
    aod_tab = application.app_tab_list[0]
    add_heading(aod_tab, 'Affiant')
    affiant_fields = Address()
    add_gender_button(aod_tab, affiant_fields)
    add_fields_from_list(aod_tab, affiant_fields)

    add_heading(aod_tab, 'Case Information')
    add_sub_heading(aod_tab, 'Applies to affiant and judge.')
    case_information_fields = CaseInformation()
    add_fields_from_list(aod_tab, case_information_fields)

    add_heading(aod_tab, 'Judge')
    judge_fields = JudgeAddress()
    add_fields_from_list(aod_tab, judge_fields)

    aod_tab.set_col_cursor(2)
    aod_tab.set_row_cursor(0)

    add_heading(aod_tab, 'AOD Requirements')
    add_sub_heading(aod_tab, 'Check the items to include in affiant rejection letter.')
    aod_req_fields = AODRequirements()
    add_multiple_checkboxes(aod_tab, aod_req_fields)

    aod_tab.set_row_cursor(8)
    add_button_left(aod_tab, 'Create Affiant Letter',
                        lambda: button_create_affiant_letter(affiant_fields,
                                case_information_fields, judge_fields, aod_req_fields))
    add_button_left(aod_tab, 'Print Affiant Label',
                        lambda: button_print_label(affiant_fields))
    aod_tab.set_row_cursor(14)
    add_button_left(aod_tab, 'Create Judge Letter', lambda: button_create_judge_letter(
                        affiant_fields, case_information_fields, judge_fields))
    add_button_left(aod_tab, 'Print Judge Label', lambda: button_print_label(judge_fields))
    aod_tab.set_row_cursor(8)
    add_button_right(aod_tab, 'Clear Affiant', lambda: clear_affiant(affiant_fields,
                          aod_req_fields))
    aod_tab.set_row_cursor(11)
    add_button_right(aod_tab, 'Clear Case Information',
                        lambda: clear_fields(case_information_fields))
    aod_tab.set_row_cursor(14)
    add_button_right(aod_tab, 'Clear Judge', lambda: clear_fields(judge_fields))


"___General Letters TAB___"
def gen_tab(application):
    gen_tab = application.app_tab_list[1]
    add_heading(gen_tab, 'Recipient')
    recipient_fields = PrisonerAddress()
    add_gender_button(gen_tab, recipient_fields)
    add_fields_from_list(gen_tab, recipient_fields)

    add_heading(gen_tab, 'Templates')

    button = add_button_left(gen_tab, 'Create Not Filed Letter',
            lambda: button_create_gen_letter(recipient_fields, "Not Filed"))

    button2 = add_button_left(gen_tab, 'Create No Case Letter',
            lambda: button_create_gen_letter(recipient_fields, "No Case"))

    button3 = add_button_left(gen_tab, 'Create No Forms Letter',
            lambda: button_create_gen_letter(recipient_fields, "No Forms"))

    gen_tab.set_col_cursor(2)
    gen_tab.set_row_cursor(2)

    add_button_left(gen_tab, 'Print Label',lambda: button_print_label(recipient_fields))
    gen_tab.set_col_cursor(3)
    gen_tab.set_row_cursor(2)
    add_button_left(gen_tab, 'Clear Recipient',lambda: clear_fields(recipient_fields))

    gen_tab.set_row_cursor(11)
    gen_tab.set_col_cursor(1)

    add_heading(gen_tab, 'Letter Preview')
    field = add_preview_field(gen_tab, "test")
    button_ttp = CreatePreview(button, field, GEN_NotFiledLetter.return_preview())
    button2_ttp = CreatePreview(button2, field, GEN_NoCaseLetter.return_preview())
    button3_ttp = CreatePreview(button3, field, GEN_NoFormsLetter.return_preview())
