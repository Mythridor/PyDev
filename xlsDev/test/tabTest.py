#! /usr/local/bin/Python3.6

import xlwt
from xlrd import open_workbook

wb2 = xlwt.Workbook()
s = wb2.add_sheet('Evaluation', cell_overwrite_ok=True)

wb = open_workbook("test.xls")
s2 = wb.sheet_by_index(0)
listeComp = [
    [1, 2, 3],
    [1, 4, 5],
    [1, 6, 7]
]

range = range(0, 3)
for y in range:
    for x in range:
        condition = s2.cell(y - 1, x).value == s2.cell(y, x).value and y - 1 >= 0
        s.write(y, x, listeComp[y][x])
        if condition:
            print(str(condition) + ":" + str(y - 1) + "/" + str(y) + "/" + str(x))
            s.write_merge(y - 1, y + 1, x, x, listeComp[y][x])

wb2.save('test.xls')
