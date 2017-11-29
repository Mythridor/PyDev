from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def get_skills():
    matrix = open_workbook("matrix.xls", formatting_info=True).sheet_by_index(1)
    liste=list()
    for row_x in range(3,matrix.nrows):
        intermediaire = list()
        for col_x in range(0,4):
            intermediaire.append(matrix.cell(row_x, col_x).value)
        liste.append(intermediaire)
    liste.pop(-1) # suppression d'une liste vide
    #print(liste)
    return liste
#a = get_skills()
#print(a[45])
    #for i in liste:
     #   print(i)
#final()