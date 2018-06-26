# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Hight_people = int(input("你的身高(cm)? :"))
Weight_people = int(input("你的體重(kg)? :"))

BMI = Weight_people/((Hight_people/100)**2)
if(BMI>=28):health = "肥胖"
elif(BMI>=24):
    health = "超重"
elif(BMI>=18.5):
    health = "正常體重"
else:
    health = "過輕"
print("你的BMI值為%.2f, %s"%(BMI,health))
input("按任意建後結束...")