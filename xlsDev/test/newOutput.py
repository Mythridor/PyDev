from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def output():
    source = open_workbook("ASIP_source.xls", formatting_info=True) # Ouverture du fichier ASIP_source.xls
    wb = copy(source) # Passage de format xlrd à xlwt
    ws = wb.get_sheet(1) # Sélection de la page "Entretien Evaluation" dans fichier source

    ###### Formatage
    plain = easyxf('font: name Calibri, height 220; \
    alignment: horizontal center, vertical center; \
    pattern: pattern solid,fore_color yellow')
    #######

    ws.write(2,2,"Test",plain) # Ecriture dans row 2, colonne 2
    wb.save("mystesto.xls") # Sauvegarde

output()