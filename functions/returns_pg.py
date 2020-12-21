# -*- coding: utf-8 -*-
import random


def total(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = i + total
    return total

    
def division(start, end, can_div, cannot_div, step=1):
    num_list = []
    for i in range(start, end, step):
        if i % can_div == 0 and i % cannot_div != 0:
            num_list.append(i)
    return num_list
    
    
def times(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        if i <= end:
            total = total + 1
    return total


def numOfSentence(role_a=1, role_b=1):
    pan = 0
    if role_a == 1 and role_b == 1:
        pan = 10
    elif role_a == 0 and role_b == 1:
        pan = 20
    elif role_a == 1 and role_b == 0:
        pan = 30
    else:
        pan = 3
    return pan



t = total(1, 101, 3)
print(t)

#a
if t>200:
    print('ok')
    
    
#b
print('他们的和为：%s' %t)
