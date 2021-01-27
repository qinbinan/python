# -*- coding: utf-8 -*-


# i=1    j=1
# i=2    j=1   j=2
# i=3    j=1   j=2   j=3
# i=4    j=1   j=2   j=3   j=4
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):  
        print('{}x{}={}\t'.format(j, i, i*j), end='')
        #print('%d*%d=%d\t' %(i,j,i*j))
    print()