# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:59:29 2024

@author: Nguyễn Thị Thanh Thùy 2304131
"""
import math
a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
if a > 0 and b > 0 and a != b:
    A= ((((a+b)/((a**1/3)+(b**1/3))- (a*b)**1/3))/((a**1/3) -(b**1/3))**2)
    print("ket qua cua bieu thuc A la:",A)
else:
    print("khong hop le")