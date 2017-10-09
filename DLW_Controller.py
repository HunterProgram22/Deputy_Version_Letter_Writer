from tkinter.filedialog import askopenfilename
from tkinter import messagebox, END
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os, docx, time, sys
from DLW_Templates import *
from DLW_Labels import print_label

DATE_LETTER = time.strftime("%B %d, %Y")
DATE_FILENAME = time.strftime("%m-%d-%y")

def open_blank_file():
    os.startfile(TEMPLATE)

def open_existing_AOD_file():
    name = askopenfilename(initialdir=AOD_FILEPATH)
    if name:
        os.startfile(name)
    else:
        return None

def open_existing_GEN_file():
    name = askopenfilename(initialdir=GEN_FILEPATH)
    if name:
        os.startfile(name)
    else:
        return None

def open_doc(document):
    if messagebox.askyesno("Modify Template?",
            "If you modify the template and then save the changes they are permanent " +\
            "and future letters will incorporate the changes, do you want to proceed?"):
        os.startfile(document)
    else:
        return None

def print_doc(document):
    os.startfile(document, "print")

def application_exit():
    exit()

def button_create_affiant_letter(affiant_fields, case_information_fields,
        judge_fields, aod_req_fields):
    fields = aod_return_field_values(affiant_fields, case_information_fields,
            judge_fields, aod_req_fields)
    letter = AOD_AffiantLetter(fields)
    letter.create_letter()

def button_create_judge_letter(affiant_fields, case_information_fields,
        judge_fields):
    fields = aod_return_field_values(affiant_fields, case_information_fields,
            judge_fields)
    letter = AOD_JudgeLetter(fields)
    letter.create_letter()

def button_create_gen_letter(recipient, letter_type):
    """Make this function a dictionary??"""
    fields = gen_return_field_values(recipient)
    if letter_type == "Not Filed":
        letter = GEN_NotFiledLetter(fields)
    elif letter_type == "No Case":
        letter = GEN_NoCaseLetter(fields)
    elif letter_type == "No Forms":
        letter = GEN_NoFormsLetter(fields)
    else:
        letter = GEN_Letter(fields)
    letter.create_letter()

def button_create_jur_letter(recipient, letter_type):
    """Make this function a dictionary??"""
    fields = jur_return_field_values(recipient)
    if letter_type == "Late JUR":
        letter = GEN_LateJurLetter(fields)
    elif letter_type == "Late JUR Delayed Appeal":
        letter = GEN_LateJurDelayedAppealLetter(fields)
    elif letter_type == "Timely JUR Missing Docs":
        letter = GEN_TimelyJurMissingDocsLetter(fields)
    else:
        letter = GEN_Letter(fields)
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
    #newstring = ""
    #for paragraph in string.paragraphs:
    #    newstring = newstring + '\n' + paragraph.text
    return string

def aod_return_field_values(affiant, case_information, judge, tab):
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
    field_values["rejection_reasons"] = assemble_rejection_reasons(tab)
    field_values["judge_first_name"] = judge.first_name.get()
    field_values["judge_last_name"] = judge.last_name.get()
    field_values["judge_address"] = judge.address.get()
    field_values["judge_city"] = judge.city.get()
    field_values["judge_state"] = judge.state.get()
    field_values["judge_zipcode"] = judge.zipcode.get()
    field_values["date"] = DATE_LETTER
    return field_values

def gen_return_field_values(recipient_fields):
    field_values = {}
    if recipient_fields.gender.get() == 1:
        field_values["prefix"] = "Mr."
    else:
        field_values["prefix"] = "Ms."
    field_values["first_name"] = recipient_fields.first_name.get()
    field_values["last_name"] = recipient_fields.last_name.get()
    field_values["inmate_number"] = recipient_fields.inmate_number.get()
    field_values["prison"] = recipient_fields.prison.get()
    field_values["address"] = recipient_fields.address.get()
    if recipient_fields.address_2.get() == "None":
        field_values["address2"] = ""
    else:
        field_values["address2"] = recipient_fields.address_2.get()
    field_values["city"] = recipient_fields.city.get()
    field_values["state"] = recipient_fields.state.get()
    field_values["zipcode"] = recipient_fields.zipcode.get()
    field_values["date"] = DATE_LETTER
    return field_values

def jur_return_field_values(recipient_fields):
    field_values = {}
    if recipient_fields.gender.get() == 1:
        field_values["prefix"] = "Mr."
    else:
        field_values["prefix"] = "Ms."
    field_values["first_name"] = recipient_fields.first_name.get()
    field_values["last_name"] = recipient_fields.last_name.get()
    field_values["inmate_number"] = recipient_fields.inmate_number.get()
    field_values["prison"] = recipient_fields.prison.get()
    field_values["address"] = recipient_fields.address.get()
    if recipient_fields.address_2.get() == "None":
        field_values["address2"] = ""
    else:
        field_values["address2"] = recipient_fields.address_2.get()
    field_values["city"] = recipient_fields.city.get()
    field_values["state"] = recipient_fields.state.get()
    field_values["zipcode"] = recipient_fields.zipcode.get()
    field_values["coa_decision_date"] = recipient_fields.coa_decision_date.get()
    field_values["appeal_due_date"] = recipient_fields.appeal_due_date.get()
    field_values["document_received_date"] = recipient_fields.document_received_date.get()
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

def clear_all():
    pass

def main():
    pass

if __name__ == '__main__':
    main()
