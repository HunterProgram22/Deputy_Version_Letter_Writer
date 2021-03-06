from tkinter.filedialog import askopenfilename
from tkinter import messagebox, END
from docx.enum.text import WD_ALIGN_PARAGRAPH
from os import path, startfile
from win32com.client import Dispatch
import docx, time, sys
from DLW_Models import AOD_AffiantLetter, AOD_JudgeLetter

DATE_LETTER = time.strftime("%B %d, %Y")
AOD_FILEPATH = 'S:\\AOD\\2017'
GEN_FILEPATH = 'S:\\Deputy Clerks'
PATH = 'S:\\AOD\\AOD_Test\\'
TEMPLATE_PATH = "S:\\Letter_Writer\\Templates\\"
TEMPLATE = TEMPLATE_PATH + 'Template.docx'

def open_blank_file():
    startfile(TEMPLATE)

def open_existing_AOD_file():
    name = askopenfilename(initialdir=AOD_FILEPATH)
    if name:
        startfile(name)
    else:
        return None

def open_existing_GEN_file():
    name = askopenfilename(initialdir=GEN_FILEPATH)
    if name:
        startfile(name)
    else:
        return None

def open_doc(document):
    if messagebox.askyesno("Modify Template?",
            "If you modify the template and then save the changes they are permanent " +\
            "and future letters will incorporate the changes, do you want to proceed?"):
        startfile(document)
    else:
        return None

def print_doc(document):
    startfile(document, "print")

def application_exit():
    exit()

def button_create_affiant_letter(affiant_fields, case_information_fields,
        judge_fields, aod_req_fields):
    fields = aod_return_field_values(affiant_fields, case_information_fields,
            judge_fields, aod_req_fields)
    letter = AOD_AffiantLetter(fields)
    letter.create_letter()

def button_create_judge_letter(affiant_fields, case_information_fields,
        judge_fields, aod_req_fields):
    fields = aod_return_field_values(affiant_fields, case_information_fields,
            judge_fields, aod_req_fields)
    letter = AOD_JudgeLetter(fields)
    letter.create_letter()

def button_create_gen_letter(*args):
    recipient_fields = args[0]
    fields = recipient_fields.get_data_in_data_fields()
    letter_type = args[1]
    letter = letter_type(fields)
    letter.create_letter()

def button_print_label(recipient):
    print_label(recipient)

def print_field_values(tab):
    field_values = {}
    for field in tab:
        field_values[field] = tab.field.get()
    print(field_values)

def assemble_rejection_reasons(aod_req_fields):
    rejection_reasons = []
    for item in aod_req_fields.return_requirements_list():
        if item[1].get() == 1:
            rejection_reasons.append(item[2])
    string = "" # for use in trying to get bullet list - docx.Document(TEMPLATE)
    for j, reason in enumerate(rejection_reasons):
        string = string + '\u2022 ' + reason + '\n\n'
    return string

def aod_return_field_values(affiant, case_information, judge, aod_req_fields):
    """Look into making this the same as Gen Letters and use method under models."""
    field_values = {}
    if affiant.gender.get() == 1:
        field_values["prefix"] = "Mr."
    else:
        field_values["prefix"] = "Ms."
    field_values["affiant_first_name"] = affiant.first_name.get()
    field_values["affiant_last_name"] = affiant.last_name.get()
    field_values["affiant_address"] = affiant.address.get()
    field_values["affiant_city"] = affiant.city.get()
    field_values["affiant_state"] = affiant.state.get()
    field_values["affiant_zipcode"] = affiant.zipcode.get()
    field_values["case_name"] = case_information.case_name.get()
    field_values["case_number"] = case_information.case_number.get()
    field_values["court_name"] = case_information.court_name.get()
    field_values["rejection_reasons"] = assemble_rejection_reasons(aod_req_fields)
    field_values["judge_first_name"] = judge.first_name.get()
    field_values["judge_last_name"] = judge.last_name.get()
    field_values["judge_address"] = judge.address.get()
    field_values["judge_city"] = judge.city.get()
    field_values["judge_state"] = judge.state.get()
    field_values["judge_zipcode"] = judge.zipcode.get()
    field_values["date"] = DATE_LETTER
    return field_values

def clear_affiant(affiant, aod_reqs):
    for field in affiant.data_fields:
        field[1].set('')
    for field in aod_reqs.aod_requirements_list:
        field[1].set(0)

def clear_fields(fields):
    for field in fields.data_fields:
        field[1].set('')

def print_label(address):
    curdir = None
    if getattr(sys, 'frozen', False):
    	curdir = path.dirname(sys.executable)
    else:
    	curdir = path.dirname(path.abspath(__file__))
    mylabel = path.join(curdir,'my.label')
    num_labels = 1
    labelCom = Dispatch('Dymo.DymoAddIn')
    labelText = Dispatch('Dymo.DymoLabels')
    isOpen = labelCom.Open(mylabel)
    selectPrinter = 'DYMO LabelWriter 450'
    labelCom.SelectPrinter(selectPrinter)
    try:
        label_name = address.first_name.get() + ' ' + address.last_name.get() +\
                ' ' + address.inmate_number.get()
        label_institution = address.prison.get()
    except AttributeError:
        label_name = address.first_name.get() + ' ' + address.last_name.get()
    first_address = address.address.get()
    if first_address == "None":
        first_address = ""
    try:
        second_address = address.address_2.get()
        if second_address == "None":
            second_address = ""
        label_address = first_address + ' ' + second_address
    except AttributeError:
        label_address = first_address
    label_city_state_zip = address.city.get() + ' ' + address.state.get() +\
            ' ' + address.zipcode.get()
    try:
        if label_institution == "":
            labelText.SetField('TEXTO1', label_name)
            labelText.SetField('TEXTO2', label_address)
            labelText.SetField('TEXTO3', label_city_state_zip)
        else:
            labelText.SetField('TEXTO1', label_name)
            labelText.SetField('TEXTO2', label_institution)
            labelText.SetField('TEXTO3', label_address)
            labelText.SetField('TEXTO4', label_city_state_zip)
    except UnboundLocalError:
        labelText.SetField('TEXTO1', label_name)
        labelText.SetField('TEXTO2', label_address)
        labelText.SetField('TEXTO3', label_city_state_zip)
    labelCom.StartPrintJob()
    labelCom.Print(num_labels,False)
    labelCom.EndPrintJob()
