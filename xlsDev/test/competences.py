from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def liste_competences():
    matrix = open_workbook("matrix.xls",formatting_info=True).sheet_by_index(2)
    liste = set()
    for row_x in range(0,matrix.nrows):
        cell = matrix.cell(row_x,1)
        if cell.value =='':
            continue
        else:
            liste.add(cell.value)
    for i in liste:
        print(i)
liste_competences()