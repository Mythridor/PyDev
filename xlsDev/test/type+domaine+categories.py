from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook

def final():
    matrix = open_workbook("matrix.xls", formatting_info=True).sheet_by_index(1)
    liste=[]
    dico ={}

    for row_x in range(3,matrix.nrows):
        for col_x in range(0,3):
            #cell = matrix.cell(row_x,col_x)
            #try:
            if matrix.cell(row_x,0).value == '':
                pass
            elif matrix.cell(row_x,col_x).value !='':
                dico[matrix.cell(row_x,0).value]=list()
                col_x+=1
                dico[matrix.cell(row_x, 0).value].append(matrix.cell(row_x, col_x).value)
            #else:
             #       if matrix.cell(row_x,col_x).value == '':
              #          dico[matrix.cell(row_x, 0).value].append(' ')
                #    dico[matrix.cell(row_x,0).value].append(matrix.cell(row_x,col_x))
            #except KeyError:
            #    continue
        print(dico)
final()