# -*- coding: utf-8 -*-
from pymysql import connect


# arguments
def total(*args):
    total = 0
    for i in range(args[0], args[1], args[2]):
        total = i + total
    
    print('1+2+3+....+100的和:%s' % total)

# total(1,101,4)


def total2(**kwargs):
    total = 0
    for i in range(kwargs['start'], kwargs['end'], kwargs['step']):
        total = i + total
    
    print('1+2+3+....+100的和:%s' % total)
    print(kwargs['caichang'])

    
total2(start=1, end=101, step=3, caichang='凤姐')


def addCustomer(cname, **kwargs):
    pass


