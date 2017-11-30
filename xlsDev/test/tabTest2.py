#! /usr/local/bin/Python3.6

from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def writeout(lista):
    source = open_workbook("test.xls", formatting_info=True)  # Ouverture du fichier test.xls
    wb = copy(source)  # Passage de format xlrd à xlwt
    #ns = wb.add_sheet("Test-ecriture", cell_overwrite_ok=True)  # Création d'une feuille vierge pour tester
    ws = wb.get_sheet(0)  # Sélection de la page "Test-ecriture" dans fichier source
    buffer = 19
    plain = easyxf('font: name Calibri, height 220')
    for count, data in enumerate(lista):
        # count est le compteur de lignes (c'est un chiffre integer)
        # data (qui est une liste) correspond à l'item numéro "count" de Skill4Job (data = Skill4Job[count])
        for element in range(0, 4):
            # element est l'index entre 0 et 4 pour chaque élément de la liste data
            offset = count + buffer # chaque count est décalée de 20 lignes.
            ws.write(offset,element,data[element],plain) # ici element correspond également à la colonne de chaque liste
            print(data[element], offset)
    wb.save('output_write.xls')