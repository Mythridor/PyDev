from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook
def output():
    source = open_workbook("ASIP_source.xls", formatting_info=True)
    wb = copy(source)
    ws = wb.get_sheet(0)

    #sheet_test1 = book.add_sheet("test1")
    #sheet_test1.write(0,0,"Première colonne")
    #sheet_test1.write(0,1,"Deuxième colonne")
    plain = easyxf('font: name Calibri, height 220; alignment: horizontal center, vertical center; pattern: pattern solid,fore_color yellow')
    ws.write(2,3,"Test",plain)
    wb.save("mystesto.xls")
    #print(xls_write)
output()