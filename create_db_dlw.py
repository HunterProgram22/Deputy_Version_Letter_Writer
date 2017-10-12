from tinydb import TinyDB, Query

TEMPLATE_PATH = "S:\\Letter_Writer\\Templates\\"

db = TinyDB(TEMPLATE_PATH + 'Templates.json')
db.insert({'name': 'Affiant_Template', 'docpath': 'Affiant_Template.docx'})
db.insert({'name': 'Gen_Template', 'docpath': 'Gen_Template.docx'})
db.insert({'name': 'Judge_Template', 'docpath': 'Judge_Template.docx'})
db.insert({'name': 'NotFiled_Template', 'docpath': 'NotFiled_Template.docx'})
db.insert({'name': 'NoCase_Template', 'docpath': 'NoCase_Template.docx'})
db.insert({'name': 'NoForms_Template', 'docpath': 'NoForms_Template.docx'})
db.insert({'name': 'LateJur_Template', 'docpath': 'LateJur_Template.docx'})
db.insert({'name': 'LateJurDelayedAppeal_Template', 'docpath': 'LateJurDelayedAppeal_Template.docx'})
db.insert({'name': 'JurMissingDocs_Template', 'docpath': 'JurMissingDocs_Template.docx'})
db.insert({'name': 'DafNoOpinion_Template', 'docpath': 'DafNoOpinion_Template.docx'})
db.insert({'name': 'DafNoFacts_Template', 'docpath': 'DafNoFacts_Template.docx'})



db.close()
