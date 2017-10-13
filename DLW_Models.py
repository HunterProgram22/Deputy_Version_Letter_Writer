from tkinter import StringVar, IntVar, Text
import time, docx, os

AOD_FILEPATH = 'S:\\AOD\\2017'
GEN_FILEPATH = 'S:\\Deputy Clerks'
PATH = 'S:\\AOD\\AOD_Test\\'
TEMPLATE_PATH = "S:\\Letter_Writer\\Templates\\"
SAVE_PATH = "S:\\Letter_Writer\\"

TEMPLATE = TEMPLATE_PATH + 'Template.docx'
AFFIANT_TEMPLATE = TEMPLATE_PATH + 'Affiant_Template.docx'
JUDGE_TEMPLATE = TEMPLATE_PATH + 'Judge_Template.docx'
GEN_TEMPLATE = TEMPLATE_PATH + 'Gen_Template.docx'
NOTFILED_TEMPLATE = TEMPLATE_PATH + 'NotFiled_Template.docx'
NOCASE_TEMPLATE = TEMPLATE_PATH + 'NoCase_Template.docx'
NOFORMS_TEMPLATE = TEMPLATE_PATH + 'NoForms_Template.docx'
LATEJUR_TEMPLATE = TEMPLATE_PATH + 'LateJur_Template.docx'
LATEJUR_DAF_TEMPLATE = TEMPLATE_PATH + 'LateJurDelayedAppeal_Template.docx'
JUR_MISSINGDOCS_TEMPLATE = TEMPLATE_PATH + 'JurMissingDocs_Template.docx'
JUR_NOEXTENSION_TEMPLATE = TEMPLATE_PATH + 'JurNoExtension_Template.docx'
DAF_NOFACTS_TEMPLATE = TEMPLATE_PATH + 'DafNoFacts_Template.docx'
DAF_NOOPINION_TEMPLATE = TEMPLATE_PATH + 'DafNoOpinion_Template.docx'
OA_NOSECDEP_TEMPLATE = TEMPLATE_PATH + 'OriginalActionNoSecurityDeposit_Template.docx'
OA_NOADD_TEMPLATE = TEMPLATE_PATH + 'OriginalActionNoAddress_Template.docx'
OA_NOTNOTARIZED_TEMPLATE = TEMPLATE_PATH + 'OriginalActionNotNotarized_Template.docx'
OA_NOADDSECDEPAFF_TEMPLATE = TEMPLATE_PATH + 'OriginalActionNoAddNoSecDepNoAff_Template.docx'

DATE_LETTER = time.strftime("%B %d, %Y")


class Address(object):
    """ A for creating a mailing address. """
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

    def get_data_in_data_fields(self):
        self.field_values = {}
        self.field_values["Date"] = DATE_LETTER
        if self.gender.get() == 1:
            self.field_values["Prefix"] = "Mr."
        else:
            self.field_values["Prefix"] = "Ms."
        for item in self.data_fields:
            if item[1].get() == "None":
                self.field_values[item[0]] = ""
            else:
                self.field_values[item[0]] = item[1].get()
        return self.field_values


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


class Letter(object):
    def __init__(self, fields):
        self.path = SAVE_PATH
        self.fields = fields
        self.letter = docx.Document(TEMPLATE)
        for paragraph in self.letter.paragraphs:
            p = paragraph._element
            p.getparent().remove(p)
            p._p = p._element = None

    def create_letter(self):
        """self.template is not initialized for superclass, in the
        subclasses it is assigned the relevant template."""
        self.master_template = docx.Document(self.template)
        self.string = ""
        for paragraph in self.master_template.paragraphs:
            self.string = self.string + '\n' + paragraph.text
        self.newstring = self.string.format(**self.fields)
        self.letter.add_paragraph(self.newstring)
        self.letter.save(self.docname)
        self.open_letter()

    def open_letter(self):
        os.startfile(self.docname)


class AOD_AffiantLetter(Letter):
    def __init__(self, fields):
        Letter.__init__(self, fields)
        self.template = AFFIANT_TEMPLATE
        self.docname = self.path + self.fields["affiant_last_name"] + ', ' +\
            self.fields["affiant_first_name"] + " (" + self.fields["date"] + ")" +\
            '.docx'

    def create_letter(self):
        """Need to modify this to put rejection reasons in an indented
        bullet list format. String, then Docx Add Paragraph, then String.
        Or if fix is done elsewhere eliminate this method."""
        self.master_template = docx.Document(self.template)
        self.string = ""
        for paragraph in self.master_template.paragraphs:
            self.string = self.string + '\n' + paragraph.text
        self.newstring = self.string.format(**self.fields)
        self.letter.add_paragraph(self.newstring)
        self.letter.save(self.docname)
        self.open_letter()


class AOD_JudgeLetter(Letter):
    def __init__(self, fields):
        Letter.__init__(self, fields)
        self.template = JUDGE_TEMPLATE
        self.docname = self.path + self.fields["judge_last_name"] + ', ' +\
            self.fields["judge_first_name"] + " (" + self.fields["date"] + ")" +\
            '.docx'


class GEN_Letter(Letter):
    def __init__(self, fields):
        Letter.__init__(self, fields)
        self.fields = fields
        self.template = GEN_Letter.get_template()
        self.docname = self.path + self.fields["Last Name"] + ', ' +\
            self.fields["First Name"] + " (" + self.fields["Date"] + ")" +\
            '.docx'

    @classmethod
    def get_template(cls):
        return GEN_TEMPLATE

    @classmethod
    def return_preview(cls):
        preview_template = docx.Document(cls.get_template())
        string = ""
        for paragraph in preview_template.paragraphs:
            string = string + '\n' + paragraph.text
        new = string.split(':', maxsplit=1)
        new = new[1].split('\n', maxsplit=2)
        return new[2:]


class GEN_NotFiledLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = NOTFILED_TEMPLATE

    @classmethod
    def get_template(cls):
        return NOTFILED_TEMPLATE


class GEN_NoCaseLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = NOCASE_TEMPLATE

    @classmethod
    def get_template(cls):
        return NOCASE_TEMPLATE


class GEN_NoFormsLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = NOFORMS_TEMPLATE

    @classmethod
    def get_template(cls):
        return NOFORMS_TEMPLATE


class JUR_LateJurLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = LATEJUR_TEMPLATE

    @classmethod
    def get_template(cls):
        return LATEJUR_TEMPLATE


class JUR_LateJurDelayedAppealLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = LATEJUR_DAF_TEMPLATE

    @classmethod
    def get_template(cls):
        return LATEJUR_DAF_TEMPLATE


class JUR_NoExtensionLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = JUR_NOEXTENSION_TEMPLATE

    @classmethod
    def get_template(cls):
        return JUR_NOEXTENSION_TEMPLATE


class JUR_TimelyJurMissingDocsLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = JUR_MISSINGDOCS_TEMPLATE

    @classmethod
    def get_template(cls):
        return JUR_MISSINGDOCS_TEMPLATE


class DAF_NoOpinionLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = DAF_NOOPINION_TEMPLATE

    @classmethod
    def get_template(cls):
        return DAF_NOOPINION_TEMPLATE


class DAF_NoFactsAffLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = DAF_NOFACTS_TEMPLATE

    @classmethod
    def get_template(cls):
        return DAF_NOFACTS_TEMPLATE


class OA_NoAddressLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = OA_NOADD_TEMPLATE

    @classmethod
    def get_template(cls):
        return OA_NOADD_TEMPLATE


class OA_NotNotarizedLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = OA_NOTNOTARIZED_TEMPLATE

    @classmethod
    def get_template(cls):
        return OA_NOTNOTARIZED_TEMPLATE


class OA_NoSecurityDepositLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = OA_NOSECDEP_TEMPLATE

    @classmethod
    def get_template(cls):
        return OA_NOSECDEP_TEMPLATE


class OA_NoAddNoSecDepNoAffLetter(GEN_Letter):
    def __init__(self, fields):
        GEN_Letter.__init__(self, fields)
        self.template = OA_NOADDSECDEPAFF_TEMPLATE

    @classmethod
    def get_template(cls):
        return OA_NOADDSECDEPAFF_TEMPLATE
