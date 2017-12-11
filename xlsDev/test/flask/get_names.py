from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import easyxf

def get_names():
    list_names = open_workbook("liste_noms.xls", formatting_info=True).sheet_by_index(0)
    liste=list()
    for row_x in range(2,list_names.nrows):
        full_row= list()
        for col_x in range(1,4):
            #if list_names.cell(row_x,col_x).value == "":
            #    pass
            full_row.append(list_names.cell(row_x, col_x).value)
        if full_row[2] != "":
            liste.append(full_row)
    #liste.pop(-1)  # suppression d'une liste vide
    #for i in liste:
    #    print(i)
    #print(len(liste))
    #return liste
    return liste
#get_names()