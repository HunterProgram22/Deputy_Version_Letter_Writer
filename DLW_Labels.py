#!/usr/bin/env python
import sys
from os import path
from win32com.client import Dispatch
from docx import Document

def print_label(address):
    curdir = None
    if getattr(sys, 'frozen', False):
    	# frozen
    	curdir = path.dirname(sys.executable)
    else:
    	# unfrozen
    	curdir = path.dirname(path.abspath(__file__))
    mylabel = path.join(curdir,'my.label')
    num_labels = 1

    labelCom = Dispatch('Dymo.DymoAddIn')
    labelText = Dispatch('Dymo.DymoLabels')
    isOpen = labelCom.Open(mylabel)
    selectPrinter = 'DYMO LabelWriter 450'
    labelCom.SelectPrinter(selectPrinter)

    label_name = address.first_name.get() + ' ' + address.last_name.get() +\
            ' ' + address.inmate_number.get()
    label_institution = address.prison.get()
    first_address = address.address.get()
    if first_address == "None":
        first_address = ""
    second_address = address.address_2.get()
    if second_address == "None":
        second_address = ""
    label_address = first_address + ' ' + second_address
    label_city_state_zip = address.city.get() + ' ' + address.state.get() +\
            ' ' + address.zipcode.get()

    if label_institution == "":
            labelText.SetField('TEXTO1', label_name)
            labelText.SetField('TEXTO2', label_address)
            labelText.SetField('TEXTO3', label_city_state_zip)
    else:
        labelText.SetField('TEXTO1', label_name)
        labelText.SetField('TEXTO2', label_institution)
        labelText.SetField('TEXTO3', label_address)
        labelText.SetField('TEXTO4', label_city_state_zip)

    labelCom.StartPrintJob()
    labelCom.Print(num_labels,False)
    labelCom.EndPrintJob()
