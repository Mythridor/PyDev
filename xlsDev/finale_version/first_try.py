#! /usr/local/bin/python3.6

from xlrd import open_workbook
from xlutils.copy import copy
from xlutils.filter import process, XLRDReader, XLWTWriter
from xlwt import easyxf


def copy2(wb):
    w = XLWTWriter()
    process(
        XLRDReader(wb, 'base.xls'),
        w
    )
    return w.output[0][1], w.style_list


def output():
    inBook = open_workbook(r"base.xls", formatting_info=True, on_demand=True)
    inSheet = inBook.sheet_by_index(0)

    wb = copy(inBook)
    outBook, outStyle = copy2(inBook)

    print(copy2(inBook))
    # xf_index = inSheet.cell_xf_index(0, 0)
    # saved_style = outStyle[xf_index]

    plain = easyxf('font: name Calibri, height 220; '
                   'borders: left thin, right thin, top thin, bottom thin; '
                   'alignment: horizontal center, vertical center; '
                   'pattern: pattern solid,fore_color white;')

    s = outBook.get_sheet(1)
    s.write_merge(19, 21, 0, 1, 'Savoir', plain)
    s.write_merge(22, 24, 0, 1, 'Savoir-faire', plain)
    s.write_merge(25, 27, 0, 1, 'Savoir-être', plain)
    outBook.save('evalFiche/test.xls')

output()
