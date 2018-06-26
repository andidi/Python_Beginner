# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:20:34 2018

@author: User
"""
size = int(input("輸入三角形大小"))
Num = range(size)
for i in Num:
    for j in Num:
        if(j+1<size-i):
            print(end=" ")
        else:
            print(end="*")
    print()
for i in Num:
    for j in Num:
        if(j<=i):
            print("*",end="")
    print()