# -*- coding: utf-8 -*-

#南航
def deduct_money():
    price = 200
    return price


#去哪儿网
def del_money():
    price = int(deduct_money()*1.1)
    print(price)
    
del_money()


#携程
def delete_money():
    level='砖石'
    if level=='初级':
        price = deduct_money()
    elif level=='中级':
        price = deduct_money()*0.9
    else:
        price = deduct_money()*0.85
    print(price)

delete_money()

