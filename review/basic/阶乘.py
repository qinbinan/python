# -*- coding: utf-8 -*-

a = int(input('请输入一个整数:'))
num = 1
if a < 0:
    print('负数没有阶乘！')
elif a == 0:
    print('0的阶乘为1！')
else :
    for i in range(1,a + 1): #a=3  1,2,3
        num = num*i
    print(num)