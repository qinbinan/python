# -*- coding: utf-8 -*-

sal = 300
comm = 20
total = sal + comm

print(total)

# 1.    // 返回商的整数部分 
# 2.    % 返回余数 
# 3.    **幂运算 

print(sal//comm)
print(sal%comm) #模，判断是不是能整除就靠它
print(comm**4)


if sal>comm:
    print('ok')
    
if sal>comm or sal>2000:
    print('good')
    
if not sal>2000:
    print('hehe')


