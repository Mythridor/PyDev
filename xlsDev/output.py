#! /usr/local/bin/Python3.5

import xlwt
from xlrd import open_workbook


def output():
    book = xlwt.Workbook()
    wb = open_workbook("input.xlsx")

    wb2 = xlwt.Workbook()
    Sheet1 = wb2.add_sheet('Evaluation')
    Sheet1.write(0, 0, 'Compétence')
    col = 1
    for mtr in range(1, 5):
        Sheet1.write(0, col, mtr)
        col += 1

    s = wb.sheet_by_index(1)
    row = 1
    subcp = 1
    for ctr in range(1, 250):
        cp = str((s.cell(ctr, 2).value).encode('utf-8').decode('utf-8'))
        print()
        print(s.cell(ctr, 5).value == 1.0)
        if s.cell(ctr, 5).value == 1.0:
            Sheet1.write(row, 0, cp)
            row += 1
        wb2.save('test.xls')


output()
