from xlrd import open_workbook

def values(col_x):
    matrix = open_workbook("matrix.xls", formatting_info=True).sheet_by_index(1)
    liste = list()
    for row_x in range(3, matrix.nrows):
        intermediaire = list()
        intermediaire.append(matrix.cell(row_x, col_x).value)
        liste.append(intermediaire)
    liste.pop(-1)  # suppression d'une liste vide
    return liste