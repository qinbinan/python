# -*- coding: utf-8 -*-

# for处理有一堆值，并要把这些值迭出来

# range(start,end,step)  start可以不写，默认从0开始，step可以不写，默认是1
# for i in range(10):
#     print(i)
    
# break 结束整个循环
# continue 结束本次循环
print('----------')
for i in range(10):
    if i != 6:
        print(i)
        continue
    print('###########')
