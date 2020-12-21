# -*-coding:UTF-8 -*-
from xlrd import open_workbook

bk = open_workbook('d:/emp.xls')
sheet = bk.sheet_by_name('empinfo')

# 读有多少行
print(sheet.nrows)

# 读有多少列
print(sheet.ncols)

# 读某单元格（9/28/1981）
cell_value = sheet.cell_value(9, 8)
print(cell_value)

# 读整个第X（9）行数据
row_values = sheet.row_values(8, 4, 9)
print(row_values)

# 读某列（编号）数据
col_values = sheet.col_values(4, 5, 14)
print(col_values)

# 读整个列表数据

emp_list = []
for i in range(4, 9):
    emp_list.append(sheet.col_values(i, 5, 14))
print(emp_list)


class Selectexcel():
    
    def __init__(self, workbook_name, sheet_name):
        self.workbook_name = workbook_name
        self.sheet_name = sheet_name

    def __sheet(self):
        bk = open_workbook(self.workbook_name)
        sheet = bk.sheet_by_name(self.sheet_name)
        return sheet
    
    def total_rows(self):
        return self.__sheet().nrows
    
    def total_cols(self):
        return self.__sheet().ncols
    
    


yolo = Selectexcel(r'd:/emp.xls', 'empinfo')
print(yolo.total_rows())    

print(yolo.total_cols())
    
    

