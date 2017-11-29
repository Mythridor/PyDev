from xlrd import open_workbook

def select_colon(fonction):
    matrice = open_workbook("matrix.xls", formatting_info=True)
    jobs = matrice.sheet_by_index(1)
    colonne =list()
    for col_x in range(0,jobs.ncols):
        cell = jobs.cell(0,col_x)
        if cell.value == fonction:
            colonne.append(col_x)
            #print(colonne)
    return colonne