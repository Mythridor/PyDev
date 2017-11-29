#! /usr/local/bin/Python3.6

import xlwt
from xlutils.copy import copy
from xlrd import open_workbook

def writeout(lista):
    source = open_workbook("test.xls", formatting_info=True)  # Ouverture du fichier test.xls
    wb = copy(source)  # Passage de format xlrd à xlwt
    #ns = wb.add_sheet("Test-ecriture", cell_overwrite_ok=True)  # Création d'une feuille vierge pour tester
    ws = wb.get_sheet(2)# Sélection de la page "Entretien Evaluation" dans fichier source
    buffer = 19
    for count, data in enumerate(lista):
        # count est le compteur de lignes (c'est un chiffre integer)
        # data correspond à l'item numéro "count" de Skill4Job (data = Skill4Job[count])
        for element in range(0, 4):
            # element est l'index entre 0 et 4 pour chaque élément de la liste data
            offset = count + buffer # chaque count est décalée de 20 lignes.
            ws.write(offset,element,data[element])
            print(data[element], offset)
            wb.save('test.xls')