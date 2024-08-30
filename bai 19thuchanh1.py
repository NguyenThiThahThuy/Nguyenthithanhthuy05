# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:57:14 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c =int(input("Nhập c:"))
d =int(input("Nhập d:"))
if a<=b and a<=c and a<=d:
    print(a)
elif b<=a and b<=c and b<= d:
    print(b)
elif c<=a and c<=b and c<=d:
    print(c)
else:
    print(d)