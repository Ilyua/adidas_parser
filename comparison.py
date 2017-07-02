import xlrd
import sys
from pprint import pprint

def comparison(path_1,path_2):
    book_1 = xlrd.open_workbook(path_1)
    sheet_1 = book_1.sheet_by_index(0)

    book_2 = xlrd.open_workbook(path_2)
    sheet_2 = book_2.sheet_by_index(0)

    Errors = []
    if sheet_1.nrows != sheet_2.nrows or sheet_1.ncols != sheet_2.ncols:
        sys.exit('Unsuitable files for comparison')
    else:
        rows = sheet_1.nrows
        columns =  sheet_1.ncols

        for row in range(rows):
            for col in range(columns):
                data_1 = sheet_1.cell_value(row,col)
                data_2 = sheet_2.cell_value(row,col)
                if data_1 != data_2:
                    Errors.append({'position': (row,col),
                                    'data_1':data_1,
                                    'data_2':data_2})
    return Errors
if __name__=='__main__':
    pprint(comparison('./adidas1.xlsx','./adidas2.xlsx'))

