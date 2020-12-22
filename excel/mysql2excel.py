# -*-coding:UTF-8 -*-
from pymysql import connect
from xlwt.Formatting import Alignment
from xlwt.Style import XFStyle
from xlwt.Workbook import Workbook

connection = connect(host='192.168.1.4', user='root',
                     password='root', database='cms', port=3306)
cursor = connection.cursor()
cursor.execute('select * from qin_student')
result = cursor.fetchall()

wb = Workbook('utf-8')
sheet = wb.add_sheet('学生信息')

title_style = XFStyle()
content_style = XFStyle()
 
alignment = Alignment()
alignment.horz = alignment.HORZ_CENTER
  
title_style.alignment = alignment
content_style.alignment = alignment  

title = ['编号', '姓名', '生日', '性别']
for i in range(len(title)):
    sheet.write(0, i, title[i], title_style)
content = result
for i in range(len(content)):
    for j in range(len(content[i])):
        sheet.write(1 + i, 0 + j, content[i][j], content_style)

cursor.close
connection.close

wb.save(r'd:/学生表.xls')
