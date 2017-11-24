#! /usr/local/bin/Python3.6

import xlwt
from xlrd import open_workbook

wb2 = xlwt.Workbook()
s = wb2.add_sheet('Evaluation', cell_overwrite_ok=True)

listeComp = [
    ["test", "a", "e"],
    ["test", "b", "f"],
    ["test", "c", "g"]
]

for row in range(0, 3):
    for col in range(0, 3):
        s.write(row, col, listeComp[row][col])

wb2.save('test.xls')

wb = open_workbook("test.xls")
s2 = wb.sheet_by_index(0)
for y in range(0, 3):
    for x in range(0, 3):
        if y - 1 >= 0 and s2.cell(y - 1, x).value == s2.cell(y, x).value:
            s.write_merge(y - 1, y + 1, x, x, listeComp[y][x])

wb2.save('test.xls')