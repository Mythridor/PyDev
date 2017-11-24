from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def type_competence():
    matrix = open_workbook("matrix.xls",formatting_info=True).sheet_by_index(1)
    liste = []
    for row_x in range(0,matrix.nrows):
        cell = matrix.cell(row_x,0)
        if cell.value == "":
            continue
        else:
            liste.append(cell.value)
    liste.pop(0)
    setto=set(liste)
    print(setto)
    return setto
type_competence()