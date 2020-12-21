# -*- coding: utf-8 -*-
import random


def total(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = i + total
    
    print('他们的和:%s' % total)

    
def division(start, end, can_div, cannot_div, step=1):
    num_list = []
    for i in range(start, end, step):
        if i % can_div == 0 and i % cannot_div != 0:
            num_list.append(i)
    print("%s以内能被%s整除但是不能被%s整除的数:%s" % (end - 1, can_div, cannot_div, num_list))
    
    
def times(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        if i <= end:
            total = total + 1
    print('%s次挑完' % total)


def numOfSentence(role_a=1, role_b=1):
    if role_a == 1 and role_b == 1:
        print('各判10年')
    elif role_a == 0 and role_b == 1:
        print('A:20年，b:1年')
    elif role_a == 1 and role_b == 0:
        print('A:1年，b:20年')
    else:
        print('各判3年')    

# total(5, 51, 3)
# total(5, 51, 5)
# total(5, 51, 1)


total(1, 101)
total(1, 101, 5)

division(1, 101, 3, 5)
# times(15, 50, 4)

numOfSentence(0, 0)
numOfSentence()
