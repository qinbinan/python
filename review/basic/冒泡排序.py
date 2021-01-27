# -*- coding: utf-8 -*-

lists=[3,5,6,2,8,1]

for i in range(1,len(lists)):
    for j in range(0,len(lists)-1):
        if lists[j]>lists[j+1]:
            lists[j],lists[j+1]=lists[j+1],lists[j]
print(lists)