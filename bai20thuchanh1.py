# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:10:38 2024

@author: Nguyễn Thị Thanh Thùy 13704131
"""
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c =int(input("Nhập c:"))
if b<=a and c<=a:
    print("Số lớn nhất:",a)
elif a<=b and c<=b :
    print("Số lớn nhất là:",b)
else:
    print("Số lớn nhất là:",c)
    