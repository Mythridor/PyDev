from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def final():
    matrix = open_workbook("matrix.xls", formatting_info=True).sheet_by_index(1)
    liste=list()
    #dico ={}
    #print(matrix.cell(32,0).value)
    for row_x in range(3,matrix.nrows):
        intermediaire = list()
        for col_x in range(0,4):
            intermediaire.append(matrix.cell(row_x, col_x).value)
        liste.append(intermediaire)
    print(liste)
final()