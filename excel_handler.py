

import openpyxl
try:
    from openpyxl.cell import get_column_letter , column_index_from_string
except ImportError:
    from openpyxl.utils import get_column_letter , column_index_from_string

def open_excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb['vule']
    cell = sheet['B3']
    if(cell.value == "le tran anh vu"):
        cell.value = "vule5726@gmail.com"
    print(sheet['B3'].value)
    print(sheet.max_row)
    print(sheet.max_column)
    print(get_column_letter(sheet.max_column)) # return AA if the max col is 27
    print(column_index_from_string("AA")) # return 27