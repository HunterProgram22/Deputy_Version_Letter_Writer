from tkinter import StringVar, IntVar, Text

class Address(object):
    """ A class model object for creating a mailing address. """
    def __init__ (self):
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.zipcode = StringVar()
        self.gender = IntVar()
        self.gender.set(1)
        self.data_fields = [ ('First Name', self.first_name),
                             ('Last Name', self.last_name),
                             ('Address', self.address),
                             ('City', self.city),
                             ('State', self.state),
                             ('Zipcode', self.zipcode),
                            ]

    def return_address_block(self):
        self.address_block = self.first_name.get() + ' ' + self.last_name.get() + '\n' +\
                self.address.get() + '\n' + self.city.get() + ' ' + self.state.get() +\
                ' ' + self.zipcode.get()
        return self.address_block

    def return_salutation_block(self):
        if self.gender.get() == 1:
            return 'Dear Mr. ' + self.last_name.get() + ':'
        elif self.gender.get() == 2:
            return 'Dear Ms. ' + self.last_name.get() + ':'

    def return_cc_block(self):
        return 'cc:  Hon. Judge ' + self.last_name.get()

    def return_data_fields(self):
        return self.data_fields


class JudgeAddress(Address):
    """ A subclass model object of the Address class that overrides
    fields for saluation and address block."""
    def return_address_block(self):
        self.address_block = 'Hon. Judge ' + self.last_name.get() + '\n' +\
                        self.address.get() + '\n' + self.city.get() + ' ' + self.state.get() +\
                        ' ' + self.zipcode.get()
        return self.address_block

    def return_salutation_block(self):
        return 'Dear Judge ' + self.last_name.get() + ':'


class PrisonerAddress(Address):
    """ A subclass model object of the Address class that also includes
    fields for prisoner number and institution. """
    def __init__(self):
        Address.__init__(self)
        self.address_2 = StringVar()
        self.inmate_number = StringVar()
        self.prison = StringVar()
        self.data_fields.insert(2, ('Prisoner Number', self.inmate_number))
        self.data_fields.insert(3, ('Institution', self.prison))
        self.data_fields.insert(5, ('Address 2', self.address_2))


class PrisonerAddressJurDates(PrisonerAddress):
    """A subclass of the PrisonerAddress object that includes variables
    for due dates."""
    def __init__(self):
        PrisonerAddress.__init__(self)
        self.coa_decision_date = StringVar()
        self.appeal_due_date = StringVar()
        self.document_received_date = StringVar()
        self.data_fields.append(('COA Decision Date', self.coa_decision_date))
        self.data_fields.append(('Appeal Due Date', self.appeal_due_date))
        self.data_fields.append(('Documents Received Date', self.document_received_date))


class AttorneyAddress(Address):
    """ A subclass model object of the Address class that also includes a
    field for attorney number. """
    def __init__(self):
        Address.__init__(self)
        self.atty_number = StringVar()
        self.data_fields.insert(2, ('Attorney Number', self.atty_number))


class POLAttorneyAddress(AttorneyAddress):
    """ A subclass model object of the AttorneyAddress class that removes
    all fields except name and attorney number."""
    def __init__(self):
        AttorneyAddress.__init__(self)
        del self.data_fields[3:]


class CaseInformation(object):
    """ A class model object that includes the case name, case number,
    and court name of a case. """
    def __init__(self):
        self.case_name = StringVar()
        self.case_number = StringVar()
        self.court_name = StringVar()
        self.data_fields = [('Case Name', self.case_name),
                            ('Case Number', self.case_number),
                            ('Court Name', self.court_name),
                            ]

    def return_data_fields(self):
        return self.data_fields

    def return_re_block(self):
        return 'Re: \t' + self.case_name.get() + ', ' + self.case_number.get() +\
                ' ' + self.court_name.get()


class POLCaseInformation(CaseInformation):
    """ A subclass model object of the Case Information class that eliminates
    case name in data field and adds fields for dates of court orders."""
    def __init__(self):
        CaseInformation.__init__(self)
        del self.data_fields[2]
        self.application_date = StringVar()
        self.suspension_date = StringVar()
        self.probation_period = StringVar()
        self.reinstatement_date = StringVar()
        self.report_date = StringVar()
        self.suspension_description = StringVar()
        self.data_fields.insert(2, ('Suspension Date', self.suspension_date))
        self.data_fields.insert(3, ('Probation Period', self.probation_period))
        self.data_fields.insert(4, ('Reinstatement Date', self.reinstatement_date))
        self.data_fields.insert(5, ('Application (Petition) Date', self.application_date))
        self.data_fields.insert(6, ('Board Report Date', self.report_date))

    def return_re_block(self):
        return 'Re: \t' + self.case_name.get() + ', ' + self.case_number.get()


class Requirements(object):
    """An object that contains options for a user to select for inclusion
    in a letter. The options are generally requirements that a filer failed
    to comply with when submitting documents."""
    def __init__(self, name=None):
        self.name = name


class AODRequirements(Requirements):
    """A subclass of requirements model object specific to affidavits
    of disqualification."""
    def __init__(self):
        Requirements.__init__(self)
        self.cos_judge_variable = IntVar()
        self.cos_party_variable = IntVar()
        self.hearing_date_variable = IntVar()
        self.notarized_variable = IntVar()
        self.timely_variable = IntVar()
        self.case_caption_variable = IntVar()
        self.aod_requirements_list = [
                        ('Did not serve the judge', self.cos_judge_variable,
                                'Does not include a certificate of service indicating it ' + \
                                'has been served on the judge(s) named in the affidavit.'),
                        ('Did not serve all parties', self.cos_party_variable,
                                'Does not include a certificate of service indicating it has ' + \
                                'been served on all parties or their counsel in the underlying case.'),
                        ('Does not have next hearing date', self.hearing_date_variable,
                                'Does not indicate the date of the next scheduled hearing or ' + \
                                'a statement that no hearings are scheduled.'),
                        ('The affidavit is not notarized', self.notarized_variable,
                                'Was not properly notarized with a notary public’s jurat.'),
                        ('Submitted less than 7 days before next hearing', self.timely_variable,
                                'Was not submitted seven or more days before the next scheduled ' + \
                                'hearing in the underlying case or does not include an affirmative ' + \
                                'statement that it was impossible to file before seven days and ' + \
                                'gives reason why it was impossible.'),
                        ('Affidavit is missing lower court case information', self.case_caption_variable,
                                'Does not indicate the underlying case caption and case number.'),
                        ]

    def return_requirements_list(self):
        return self.aod_requirements_list

    def return_affiant_body_block(self):
        self.affiant_body_block = []
        for item in self.aod_requirements_list:
            if item[1].get() == 1:
                self.affiant_body_block.append(item[2])
        return self.affiant_body_block
