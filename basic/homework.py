# -*- coding: utf-8 -*-
import random
from random import choice

# 1+2+3+....+100的和
total = 0
for i in range(1, 101):
    total = i + total

print('1+2+3+....+100的和:%s' % total)

# 100以内能被3整除但是不能被5整除的数
# 把这些数弄成一个列表
num_list = []
for i in range(101):
    if i % 3 == 0 and i % 5 != 0:
        num_list.append(i)
print("100以内能被3整除但是不能被5整除的数:%s" % num_list)

# 有一个水缸，能装50L水，现在已经有了15L，每次挑水只能挑4L，几次能挑满
total = 0

for i in range(0, 50, 4):
    if i <= 50 - 15:
        total = total + 1

print('%s次可以挑完' % total)

# 写一个竞猜游戏，用户必须猜一个秘密的数字，在每次猜完后程序会告诉用户他猜的数是太大了还是太小了，
# 直到猜测正确，最后打印出猜测的次数。如果用户连续猜测同一个数字则只算一次。

# me = random.randint(1, 100)
# total = 0
# print(me)
# for i in range(1001):
#     guess = int(input('请输入你要猜测的数（1-100包含1和100）：'))
#     if guess > me:
#         total = total + 1
#         print('大了')
#     elif guess < me:
#         total = total + 1
#         print('小了')
#     else:
#         total = total + 1
#         print('猜对了，喝酒吧,我们测了%s次才正确' % total)
#         break

# lists = ['石头', '剪刀', '布']
# computer_choice = choice(lists)
# my_choice = input('我输入的规则（只能石头、剪刀、布）：')
# 
# print(computer_choice)
# print(my_choice)
# 
# if computer_choice == my_choice:
#     print('平局')
# elif (computer_choice == '剪刀' and my_choice == '布') or (computer_choice == '石头' and my_choice == '剪刀') or (computer_choice == '布' and my_choice == '石头'):
#     print('电脑获胜')
# else:
#     print('我获胜')
    
a = int(input('法官说：A，你认罪吗？（1或0,1认罪，0不认罪）'))
b = int(input('法官说：B，你认罪吗？（1或0,1认罪，0不认罪）'))
if a == 1 and b == 1:
    print('各判10年')
elif a == 0 and b == 1:
    print('A20年，b1年')
elif a == 1 and b == 0:
    print('A1年，b20年')
else:
    print('各判3年')
