from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def select_job():
    matrice = open_workbook("matrix.xls", formatting_info=True)
    comp = matrice.sheet_by_index(1)
    liste=[]
    for col_x in range(0,comp.ncols):
        cell = comp.cell(0,col_x)
        if cell.value == '':
            continue
        else:
            #print(cell.value)
            liste.append(cell.value)
        #liste.pop[0]
        #liste.pop[-1]
        #for i in liste:
    liste.pop(0)
    liste.pop(-1)
    print(liste)
    return liste
select_job()