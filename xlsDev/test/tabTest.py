#! /usr/local/bin/Python3.6

import xlwt
from xlrd import open_workbook

wb2 = xlwt.Workbook()
s = wb2.add_sheet('Evaluation', cell_overwrite_ok=True)

listeComp = [
    ["test", "a", "e"],
    ["test", "b", "f"],
    ["test", "b", "g"],
    ["test", "d", "g"]
]

range_y = range(0, len(listeComp))
range_x = range(0, len(listeComp[0]))

for row in range_y:
    for col in range_x:
        s.write(row, col, listeComp[row][col])

wb2.save('test.xls')

# wb = open_workbook("test.xls")
# s2 = wb.sheet_by_index(0)
# n = 0
# for row in range_y:
#    for col in range_x:
#        print(row, " ", row - n, " ", n, col == (len(range_x) - 1))
#        # print((s2.cell(row - 1, col).value == s2.cell(row, col).value), ":", s2.cell(row - 1, col).value, "[", row - 1,"] / ", s2.cell(row, col).value, "[", row, "] ")
#        if (row - 1 >= 0) and (s2.cell(row - 1, col).value == s2.cell(row, col).value):
#            s.write_merge(row - n, row, col, col, listeComp[row][col])
#
#        if col == (len(range_x) - 1):
#            n += 1
#
# wb2.save('test.xls')
