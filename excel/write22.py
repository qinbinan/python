# -*-coding:UTF-8 -*-
from xlwt.Workbook import Workbook
from xlwt.Formatting import Alignment
from xlwt.Style import XFStyle
# wb = Workbook('utf-8')
# sheet = wb.add_sheet('test')
# sheet.write(2, 2, 'test')
# wb.save(r'd:/test.xls')

wb = Workbook('utf-8')
sheet = wb.add_sheet('test2')
title = ['编号', '姓名', '职业', '上级', '入职日期']
 
title_style = XFStyle()
content_style = XFStyle()
 
alignment = Alignment()
alignment.horz = alignment.HORZ_CENTER
  
title_style.alignment = alignment
content_style.alignment = alignment    
 
for i in range(len(title)):
    sheet.write(0, i, title[i], title_style)
 
content = [[7369, 'SMITH', 'CLERK', 7902, '12/17/1980'],
           [7499, 'ALLEN', 'SALESMAN', 7698, '2/20/1981'],
           [7521, 'WARD', 'SALESMAN', 7698, '2/22/1981'],
           [7566, 'JONES', 'MANAGER', 7839, '4/2/1981'],
           [7654, 'MARTIN', 'SALESMAN', 7698, '9/28/1981'],
           [7698, 'BLAKE', 'MANAGER', 7839, '5/1/1981'],
           [7782, 'CLARK', 'MANAGER', 7839, '6/9/1981'],
           [7788, 'SCOTT', 'ANALYST', 7566, '4/19/1987'],
           [7839, 'KING', 'PRESIDENT', None, '11/17/1981']]
 
for i in range(len(content)):
    for j in range(len(content[i])):
        sheet.write(1 + i, 0 + j, content[i][j], content_style)
 
wb.save(r'd:/test2.xls')


from xlrd import open_workbook
from xlutils.copy import copy
ori_excel = open_workbook(r'd:/test2.xls', formatting_info=True)
new_excel = copy(ori_excel)
sheet = new_excel.get_sheet(0)
 
content_style = XFStyle()
alignment = Alignment()
alignment.horz = alignment.HORZ_CENTER
content_style.alignment = alignment    
 
# sheet.write(10,0,7777,content_style)
# sheet.write(10,1,'BYRON',content_style)
 
new_per=[7777,'BYRON','CLERK',7902,'12/10/2020']
for i in range(len(new_per)):
    sheet.write(10,i,new_per[i],content_style)
 
new_excel.save(r'd:/test3.xls')


















