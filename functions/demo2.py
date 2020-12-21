# -*- coding: utf-8 -*-
from random import choice
import random


def total():
    total = 0
    for i in range(1, 101):
        total = i + total
    
    print('1+2+3+....+100的和:%s' % total)
    
    
def division():
    num_list = []
    for i in range(101):
        if i % 3 == 0 and i % 5 != 0:
            num_list.append(i)
    print("100以内能被3整除但是不能被5整除的数:%s" % num_list)
    
    
def times():
    total = 0
    for i in range(15, 50, 4):
        if i <= 50:
            total = total + 1
    print('%s次挑完' %total())


def finger_guess():
    me = random.randint(1, 100)
    total = 0
    print(me)
    for i in range(1001):
        guess = int(input('请输入你要猜测的数（1-100包含1和100）：'))
        if guess > me:
            total = total + 1
            print('大了')
        elif guess < me:
            total = total + 1
            print('小了')
        else:
            total = total + 1
            print('猜对了，喝酒吧,我们测了%s次才正确' % total)
            break
        
        
def game_of_simple():
    lists = ['石头', '剪刀', '布']
    computer_choice = choice(lists)
    my_choice = input('我输入的规则（只能石头、剪刀、布）：')
     
    print(computer_choice)
    print(my_choice)
     
    if computer_choice == my_choice:
        print('平局')
    elif (computer_choice == '剪刀' and my_choice == '布') or (computer_choice == '石头' and my_choice == '剪刀') or (computer_choice == '布' and my_choice == '石头'):
        print('电脑获胜')
    else:
        print('我获胜')
        
    
def numOfSentence():
    role_a = int(input('法官说：A，你认罪吗？（1或0,1认罪，0不认罪）'))
    role_b = int(input('法官说：B，你认罪吗？（1或0,1认罪，0不认罪）'))
    if role_a == 1 and role_b == 1:
        print('各判10年')
    elif role_a == 0 and role_b == 1:
        print('A:20年，b:1年')
    elif role_a == 1 and role_b == 0:
        print('A:1年，b:20年')
    else:
        print('各判3年')
