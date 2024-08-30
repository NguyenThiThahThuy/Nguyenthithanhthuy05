# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:49:36 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
d = int(input("Nhap so d:"))
Tong = a + b + c + d
if 0<Tong<10 :
    print("So nut xe la:", Tong)
elif Tong>9:
    sonut = Tong//10+ Tong%10 
    print("So nut xe la:", sonut -1 )
else:
    print("khong xac dinh")
