from xlwt import easyxf
from xlutils.copy import copy
from xlrd import open_workbook
def output():
    source = open_workbook("ASIP_source.xlsx", formatting_info=True)
    s = source.sheet_by_index(0)

    #sheet_test1 = book.add_sheet("test1")
    #sheet_test1.write(0,0,"Première colonne")
    #sheet_test1.write(0,1,"Deuxième colonne")


    Nom = s.write(5,1,"Test")
    source.save("mystesto.xlsx")

output()