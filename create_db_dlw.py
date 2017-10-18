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
db.insert({'name': 'LateBrief_Template', 'docpath': 'LateBrief_Template.docx'})
db.insert({'name': 'LateRecon_Template', 'docpath': 'LateRecon_Template.docx'})
db.insert({'name': 'NoRecon_Template', 'docpath': 'NoRecon_Template.docx'})
db.insert({'name': 'JurMissingDocs_Template', 'docpath': 'JurMissingDocs_Template.docx'})
db.insert({'name': 'DafNoOpinion_Template', 'docpath': 'DafNoOpinion_Template.docx'})
db.insert({'name': 'DafNotAllowed_Template', 'docpath': 'DafNotAllowed_Template.docx'})
db.insert({'name': 'DafNoFacts_Template', 'docpath': 'DafNoFacts_Template.docx'})
db.insert({'name': 'OriginalActionNoSecurityDeposit_Template', 'docpath': 'OriginalActionNoSecurityDeposit_Template.docx'})
db.insert({'name': 'OriginalActionNoAddress_Template', 'docpath': 'OriginalActionNoAddress_Template.docx'})
db.insert({'name': 'OriginalActionNotNotarized_Template', 'docpath': 'OriginalActionNotNotarized_Template.docx'})
db.insert({'name': 'OriginalActionNoAddNoSecDepNoAff_Template', 'docpath': 'OriginalActionNoAddNoSecDepNoAff_Template.docx'})
db.insert({'name': 'DapPrematureBrief_Template', 'docpath': 'DapPrematureBrief_Template.docx'})

db.close()
