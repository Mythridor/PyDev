#! /usr/local/bin/python3.6
import itertools
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
from xlutils.filter import process, XLRDReader, XLWTWriter


def copy2(wb):
    w = XLWTWriter()
    process(
        XLRDReader(wb, 'unknown.xls'),
        w
    )
    return w.output[0][1], w.style_list


def output():
    inBook = open_workbook(r"base.xls", formatting_info=True, on_demand=True)
    inSheet = inBook.sheet_by_index(0)

    # wb = copy(inBook)

    outBook, outStyle = copy2(inBook)

    print(copy2(inBook))
    # xf_index = inSheet.cell_xf_index(0, 0)
    # saved_style = outStyle[xf_index]



    # s = wb.get_sheet(1)
    # s.write(20, 0, 'A1')
    # wb.save('evalFiche/test.xls')


output()
