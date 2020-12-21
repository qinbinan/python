# -*- coding: utf-8 -*-

# 1、创建
empinfo = ()
empinfo = (7788, 'SMITH', 'CLERK', 7839, 800, None, 30)  # 插入、读某人数、批量删除
empinfo = ((1, '张飞', '涿郡屠夫'), (2, '关羽', '河北谢良'), (3, '刘备', '贵州遵义'))  # 迭出所有数据

# 2、访问:正数、负数、切片
#           0      1        2       3     4    5     6
empinfo = (7788, 'SMITH', 'CLERK', 7839, 800, None, 30)
#           -7    -6        -5     -4    - 3  -2     -1

print(empinfo[2])
print(empinfo[-5])

print(empinfo[0:4])  # [0,4)
print(empinfo[0:-3])
print(empinfo[:4])
print(empinfo[1:4])
print(empinfo[1:-3])
print(empinfo[-6:-3])
print(empinfo[-3:-6]) #空的，左边写了一个数，右边这个数一定要在前一个的右侧

empinfo = ((1, '张飞', '涿郡屠夫'), (2, '关羽', '河北谢良'), (3, '刘备', '贵州遵义'))

print(empinfo[0][2])


#3、遍历

empinfo = (7788, 'SMITH', 'CLERK', 7839, 800, None, 30)
print(empinfo[0])
print(empinfo[1])
print(empinfo[2])

print(len(empinfo)) #length

#一维迭代
for i in range(len(empinfo)):
    print(empinfo[i])
    

empinfo = ((1, '张飞', '涿郡屠夫'), (2, '关羽', '河北谢良'), (3, '刘备', '贵州遵义'))
print(empinfo[0][0])
print(empinfo[0][1])
print(empinfo[0][2])
print(empinfo[1][0])
print(empinfo[1][1])
print(empinfo[1][2])

#二维迭代
for i in range(len(empinfo)):
    for j in range(len(empinfo[i])):
        print(empinfo[i][j])
