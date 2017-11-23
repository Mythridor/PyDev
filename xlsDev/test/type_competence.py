from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def type_competence():
    matrix = open_workbook("matrix.xls",formatting_info=True).sheet_by_index(1)
    liste = set()
    for row_x in range(0,matrix.nrows):
        cell = matrix.cell(row_x,0)
        if cell.value == "":
            continue
        else:
            liste.add(cell.value)
    for i in liste:
        print(i)
    return liste
type_competence()