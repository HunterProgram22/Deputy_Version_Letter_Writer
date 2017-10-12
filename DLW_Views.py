from tkinter import Frame, Menu, W, E, Label, Entry, Radiobutton, Checkbutton, \
    Button, Text, WORD, END
import tkinter.ttk as ttk
import tkinter as tk
from DLW_Controller import *
from DLW_Addresses import PRISON_LIST, PRISON_DB
from DLW_Models import Address, JudgeAddress, CaseInformation, \
    AODRequirements, PrisonerAddress, PrisonerAddressJurDates
from tinydb import TinyDB, Query
from functools import partial

BTN_WIDTH = 20
HEADING_FONT = "Times 12 bold"
SUBHEADING_FONT = "Times 8"

TEMPLATE_PATH = "S:\\Letter_Writer\\Templates\\"
FORMS_PATH = "S:\\Letter_Writer\\Forms\\"
FAQ = FORMS_PATH + "FAQ.docx" #Frequently Asked Questions
COA = FORMS_PATH + "COA.docx" #Change of Address
AFP = FORMS_PATH + "AFP.docx" #Affidavit of Indigence

TAB_DICT = {'Delayed Appeal Letters': 0, 'Jurisdictional Letters': 1,
        'General Letters': 2, 'Original Action Letters': 3,
        'Timeliness Letters': 4, 'AOD Letters': 5,}





"""___Control Functions for Creating Widgets___"""
def add_heading(master, heading):
    heading = ttk.Label(master, text=heading, width=30, font=HEADING_FONT)
    heading.grid(row=master.row_cursor, column=master.col_cursor, columnspan=2,
            sticky=W, pady=10, padx=5)
    master.row_cursor += 1

def add_sub_heading(master, subheading):
    subheading = ttk.Label(master, text=subheading, width=50, font=SUBHEADING_FONT)
    subheading.grid(row=master.row_cursor, column=master.col_cursor, columnspan=2,
            pady=5, padx=20)
    master.row_cursor += 1

def add_gender_radiobuttons(master, model):
    male_button = Radiobutton(master, text="Mr.", variable=model.gender, value=1)
    male_button.grid(row=master.row_cursor, column=master.col_cursor, sticky=E)
    female_button = Radiobutton(master, text="Ms.", variable=model.gender, value=2)
    female_button.grid(row=master.row_cursor, column=master.col_cursor+1, sticky=W)
    master.row_cursor += 1

def add_aodtab_checkboxes(master, aod_requirements_model):
    for field in aod_requirements_model.return_requirements_list():
        box = Checkbutton(master, text=field[0], variable=field[1])
        box.grid(row=master.row_cursor, column=master.col_cursor, sticky=W)
        master.row_cursor += 1

def add_button_right(master, button_name, button_command):
    button = ttk.Button(master, text=button_name, command=button_command, width=BTN_WIDTH, style="Blue.TButton")
    button.grid(row=master.row_cursor, column=master.col_cursor, sticky=E, padx=10, pady=3)
    master.row_cursor += 1
    return button

def add_button_left(master, button_name, button_command):
    button = ttk.Button(master, text=button_name, command=button_command, width=BTN_WIDTH, style="Blue.TButton")
    button.grid(row=master.row_cursor, column=master.col_cursor, sticky=W, padx=10, pady=3)
    master.row_cursor += 1
    return button

def add_fields_from_list(master, model):
    """row_count is used to move fields to the next column when they exceed
    the number of rows available."""
    fields = model.return_data_fields()
    row_count = 0
    for field in fields:
        if row_count == 9:
            master.set_row_cursor(3)
            master.set_col_cursor (2)
        label = Label(master, text=field[0])
        label.grid(row=master.row_cursor, column=master.col_cursor, sticky=W, padx=10, pady=5)
        if field[0] == 'Institution':
            master.set_prison_field(field, model)
        else:
            entry = Entry(master, textvariable=field[1], width=20)
            entry.grid(row=master.row_cursor, column=master.col_cursor+1, pady=5)
        master.row_cursor += 1
        row_count +=1

def add_field(master, label, variable):
    label = Label(master, text=label)
    label.grid(row=master.row_cursor, column=master.col_cursor, sticky=W, padx=10, pady=5)
    entry = Entry(master, textvariable=variable, width=20)
    entry.grid(row=master.row_cursor, column=master.col_cursor+1, pady=5)
    master.row_cursor += 1

def add_text_field(master, text):
    label = Label(master, text=text)
    label.grid(row=master.row_cursor, column=master.col_cursor, sticky=W, padx=10, pady=5)
    master.text_field = Text(master, width=40, height=10, wrap=WORD)
    master.text_field.grid(row=master.row_cursor, column=master.col_cursor+1, columnspan=2, pady=5)
    master.text_field.insert("1.0", "")
    master.row_cursor += 1

def add_preview_field(master):
    widget = Text(master, height=10, wrap=WORD, font="Time 8")
    widget.grid(row=master.row_cursor, column=1, columnspan=3, rowspan=5, padx=5,
            pady=5, sticky='NSEW')
    master.grid_rowconfigure(12, weight=1)
    master.grid_rowconfigure(13, weight=1)
    master.grid_rowconfigure(14, weight=1)
    widget.insert("1.0", "")
    master.row_cursor += 1
    return widget

def create_aod_tab(application):
    aod_tab = application.app_tab_dict['AOD Letters']
    add_heading(aod_tab, 'Affiant')
    affiant_fields = Address()
    add_gender_radiobuttons(aod_tab, affiant_fields)
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
    add_aodtab_checkboxes(aod_tab, aod_req_fields)

    aod_tab.set_row_cursor(8)
    add_button_left(aod_tab, 'Create Affiant Letter', lambda: button_create_affiant_letter(
            affiant_fields, case_information_fields, judge_fields, aod_req_fields))
    add_button_left(aod_tab, 'Print Affiant Label', lambda: button_print_label(affiant_fields))
    aod_tab.set_row_cursor(14)
    add_button_left(aod_tab, 'Create Judge Letter', lambda: button_create_judge_letter(
            affiant_fields, case_information_fields, judge_fields, aod_req_fields))
    add_button_left(aod_tab, 'Print Judge Label', lambda: button_print_label(judge_fields))
    aod_tab.set_row_cursor(8)
    add_button_right(aod_tab, 'Clear Affiant', lambda: clear_affiant(
            affiant_fields, aod_req_fields))
    aod_tab.set_row_cursor(11)
    add_button_right(aod_tab, 'Clear Case Information', lambda: clear_fields(
            case_information_fields))
    aod_tab.set_row_cursor(14)
    add_button_right(aod_tab, 'Clear Judge', lambda: clear_fields(judge_fields))

def return_recipient_fields(tab_name):
    if tab_name == 'Jurisdictional Letters':
        return PrisonerAddressJurDates()
    else:
        return PrisonerAddress()

def create_tab(application, tab_name):
    """A generic tab for multiple templates with a preview window."""
    tab = application.app_tab_dict[tab_name]
    add_heading(tab, 'Recipient')
    recipient_fields = return_recipient_fields(tab_name)
    add_gender_radiobuttons(tab, recipient_fields)
    add_fields_from_list(tab, recipient_fields)
    tab.set_row_cursor(11), tab.set_col_cursor(0)
    add_heading(tab, 'Templates')
    tab.set_row_cursor(11), tab.set_col_cursor(1)
    add_heading(tab, 'Letter Preview')
    preview_field = add_preview_field(tab)
    tab.set_col_cursor(2), tab.set_row_cursor(2)
    add_button_left(tab, 'Print Label',lambda: button_print_label(recipient_fields))
    tab.set_col_cursor(3), tab.set_row_cursor(2)
    add_button_left(tab, 'Clear Recipient',lambda: clear_fields(recipient_fields))
    return (tab, preview_field, recipient_fields)

def add_template_buttons(tab, recipient_fields, template_list):
    button_list = []
    for template in template_list:
        button = add_button_left(tab, template[0], partial(button_create_gen_letter,
                recipient_fields, template[1]))
        button_list.append((button, template[1]))
    return button_list

def add_template_previews(button_list, preview_field):
    for button in button_list:
        CreatePreview(button[0], preview_field, button[1].return_preview())

# def add_radio_button_yes_no(master, question):
#     """ Initializes a radio button to answer yes or no to a statement."""
#     #master.variable = variable
#     #master.variable.set(1)
#     #ttk.Label(master, text=question, width=50, font="Times 10").grid(
#                     row=master.row_cursor, column=master.col_cursor, columnspan=2,
#                     pady=5, padx=20)
#     master.row_cursor += 1
#     Radiobutton(master, text="Yes", variable=master.variable, value=1).grid(
#                 row=self.row_cursor, column=0, sticky=E)
#     Radiobutton(master, text="No", variable=master.variable, value=2).grid(
#                 row=self.row_cursor, column=1, sticky=W)
#     master.row_cursor += 1
"""***End of Control Functions for Creating Widgets***"""

class AppWindow(ttk.Frame):
    """The main application window."""
    def __init__(self, master):
        self.tab_dict = TAB_DICT
        self.app_tab_dict = {}
        self.master = master
        self.notebook = ttk.Notebook(self.master)
        self.notebook.grid(row=1, column=0, columnspan=50, sticky='NESW')
        self.set_style()
        self.menu = AppMenu(self.master)
        for key, value in self.tab_dict.items():
                if key == 'AOD Letters':
                    self.tab = TabWindow(self.notebook)
                else:
                    self.tab = TabWindowPrisoner(self.notebook)
                self.notebook.add(self.tab, text=key)
                self.app_tab_dict[key] = self.tab

    def set_style(self):
        """Sets the style for objects on the application. Can add new styles in
        this method and they will apply to entire application."""
        self.style = ttk.Style()
        self.style.configure('Blue.TButton', font='helvetica 8', foreground='blue', padding=5)


class AppMenu(ttk.Frame):
    """The menu widget for the main application."""
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu, borderwidth=10)
        self.db = TinyDB(TEMPLATE_PATH + "Templates.JSON")
        self.file = Menu(self.menu)
        self.printdoc = Menu(self.menu)
        self.edit_templates = Menu(self.menu)
        self.file.add_command(label="New", command=open_blank_file)
        self.file.add_command(label="Open AOD Letter", command=open_existing_AOD_file)
        self.file.add_command(label="Open GEN Letter", command=open_existing_GEN_file)
        self.file.add_command(label="Exit", command=application_exit)
        self.printdoc.add_command(label="Change of Address", command=lambda: print_doc(COA))
        self.printdoc.add_command(label="Affidavit of Indigence", command=lambda: print_doc(AFP))
        self.printdoc.add_command(label="FAQ", command=lambda: print_doc(FAQ))
        for item in self.db:
            self.edit_templates.add_command(label=item['name'], command=partial(open_doc, TEMPLATE_PATH + item['docpath']))
        self.menu.add_cascade(label="File", menu=self.file)
        self.menu.add_cascade(label="Forms", menu=self.printdoc)
        self.menu.add_cascade(label="Edit_Templates", menu=self.edit_templates)


class TabWindow(ttk.Frame):
    """A class view object for creating tab windows on the main application. """
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.row_cursor = 0
        self.col_cursor = 0

    def set_col_cursor(self, column):
        self.col_cursor = column

    def set_row_cursor(self, row):
        self.row_cursor = row


class TabWindowPrisoner(TabWindow):
    """A subclass of the TabWindow that has a field for prisons and populates
    the fields with the prison address."""
    def __init__(self, master):
        TabWindow.__init__(self, master)

    def set_prison_field(self, field, model):
        """This method is used in the add_fields_from_list function that is used
        in the create_tab function which is called in Main. Perhaps refactor at
        some point in future."""
        self.model = model
        # https://stackoverflow.com/questions/38312494/show-specific-value-in-textbox-according-to-combobox-selected-value-in-python
        self.prison_field = ttk.Combobox(self, textvariable=field[1],
                    values=PRISON_LIST, width=30)
        self.prison_field.grid(row=self.row_cursor, column=1, pady=5)
        self.prison_field.bind("<<ComboboxSelected>>", self.newselection)

    def newselection(self, event):
        institution = self.prison_field.get()
        prison = PRISON_DB.get(Query()['Institution_Name'] == institution)
        self.model.address.set(prison['Address_2'])
        self.model.address_2.set(prison['Address_1'])
        self.model.city.set(prison['City'])
        self.model.state.set(prison['State'])
        self.model.zipcode.set(prison['Zipcode'])


class CreatePreview(object):
    """Create preview text for the letter when hovering on button."""
    def __init__(self, widget, destination, text):
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
