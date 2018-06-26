# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:20:34 2018

@author: User
"""
size = int(input("輸入三角形大小"))
Num = range(size)
#靠右三角
for i in Num:
    for j in Num:
        if(j+1<size-i):
            print(end=" ")
        else:
            print(end="*")
    print()
#靠左三角
for i in Num:
    for j in Num:
        if(j<=i):
            print("*",end="")
    print()
#正三角
for i in range(size+1):
    for j in range(0,size-i):
        print (end=" "),
        j += 1
    for k in range(0, 2 * i - 1):#(1,2*i)
        print (end="*")
        k += 1
    print (end="\n")
    i += 1
#菱形
for i in Num:#变量i控制行数
    for j in range(size - i):#(1,rows-i)
        print (end=" ")
        j += 1
    for k in range(2 * i - 1):#(1,2*i)
        print (end="*")
        k += 1
    print (end="\n")
    i += 1
    #菱形的下半部分
for i in Num:
    for j in range(i):#(1,rows-i)
        print (end=" ")
        j += 1
    for k in range(2 * (size - i) - 1):#(1,2*i)
        print (end="*")
        k += 1
    print (end="\n")
    i += 1
#空菱形
for i in Num:#变量i控制行数
    for j in range(size - i):#(1,rows-i)
        print (end="*")
        j += 1
    for k in range(2 * i - 1):#(1,2*i)
        print (end=" ")
        k += 1
    print (end="\n")
    i += 1
    #菱形的下半部分
for i in Num:
    for j in range(i):#(1,rows-i)
        print (end="*")
        j += 1
    for k in range(2 * (size - i) - 1):#(1,2*i)
        print (end=" ")
        k += 1
    print (end="\n")
    i += 1

   