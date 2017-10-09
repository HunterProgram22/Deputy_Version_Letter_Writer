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

    label_name = address.first_name.get() + ' ' + address.last_name.get()
    label_address = address.address.get()
    label_city_state_zip = address.city.get() + ' ' + address.state.get() +\
            ' ' + address.zipcode.get()

    labelText.SetField('TEXTO1', label_name)
    labelText.SetField('TEXTO2', label_address)
    labelText.SetField('TEXTO3', label_city_state_zip)

    labelCom.StartPrintJob()
    labelCom.Print(num_labels,False)
    labelCom.EndPrintJob()

def get_label_address(template):
    #TODO add generator to account for possible blank space or date?
    document = Document(template)
    address = []
    for paragraph in document.paragraphs[:4]:
        address.append(paragraph.text)
    return address

def print_label_template(template):
    curdir = None
    # CODE BETWEEN HERE
    if getattr(sys, 'frozen', False):
    	# frozen
        curdir = path.dirname(sys.executable)
    else:
    	# unfrozen
        curdir = path.dirname(path.abspath(__file__))
    mylabel = path.join(curdir,'my.label')
    num_labels = 1

    labelCom = Dispatch("Dymo.DymoAddIn")
    labelText = Dispatch("Dymo.DymoLabels")
    isOpen = labelCom.Open(mylabel)
    selectPrinter = 'DYMO LabelWriter 450'
    labelCom.SelectPrinter(selectPrinter)

    address = get_label_address(template)
    label_name = address[0]
    label_address = address[1]
    label_address2 = address[2]
    label_city_state_zip = address[3]

    isTrue = labelText.SetField('TEXTO1', label_name)
    labelText.SetField('TEXTO2', label_address)
    labelText.SetField('TEXTO3', label_address2)
    labelText.SetField('TEXTO4', label_city_state_zip)

    labelCom.StartPrintJob()
    labelCom.Print(num_labels,False)
    labelCom.EndPrintJob()
