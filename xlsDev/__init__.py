#! /usr/local/bin/Python3.5
import datetime

import xlwt


def output(filename, sheet, list1, list2, x, y, z):
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)

    variables = [x, y, z]
    x_desc = "Evaluateur"
    y_desc = "Evalué"
    z_desc = 'Date:'
    desc = [x_desc, y_desc, z_desc]

    col1_name = 'Compétences'
    col2_name = 'Evaluation'

    for n, (v_desc, v) in enumerate(zip(desc, variables)):
        sh.write(n, 0, v_desc)
        sh.write(n, 1, v)

    n += 2

    sh.write(n, 0, col1_name)
    sh.write(n, 1, col2_name)

    for m, e1 in enumerate(list1, n + 1):
        sh.write(m, 0, e1)

    for m, e2 in enumerate(list2, n + 1):
        sh.write(m, 1, e2)

    book.save(filename)


output("test.xls", "test", ['CP 1', 'CP 2', 'CP 3'], ['1', '2', '3'], 'Julien Favre', 'ENOU Benjamin',
       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
