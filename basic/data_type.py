# -*- coding: utf-8 -*-

# 1、判断类型用type这个函数

ename = 'smith'
print(type(ename))  # str---string

# 数值类型：整型、浮点型、字符串、空值、布尔
sal = 200
print(type(sal))

comm = 100.05
print(type(comm))

# 字符串的知识还有是一些的
# 1、即可单引号也可双引号
# 2、如果里面有各种特殊字符，建议前面加r
# 3、把字符串可以当元组来用
# 4、格式化字符串（难点）
ename = 'SMITH'
job = "CLERK"

string = "i'm ok"
print(string)

string2 = 'i\'m ok'
print(string2)

url = r'http://www.baidu.com/news?id=1'

print('我的名字叫:' + ename)  # java
print('我的名字叫:%s' % ename)  # c

print('我的名字叫:' + ename + ',我的职位是：' + job)
print('我的名字叫:%s,我的职位是：%s' % (ename, job))

is_admin = None

status = True
status = False
