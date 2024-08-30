# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:37:05 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
a=float(input("Nhập giá trị a:"))
b=float(input("Nhập gía trị b:"))
c=float(input("Nhập giá trị c:"))
delta=b**2-4*a*c
if delta<0:
    print ("Phương trình vô nghiệm")
elif delta==0:
    print ("phương trình có 1 nghiệm kép","x=",(-b/2*a))
else:
    x1 = ((-b + (delta**1/2 )) / (2 * a));
    x2 = ((-b - (delta**1/2 )) / (2 * a));
    print("phương trình có 2 nghiệm phân biệt x=",x1,"x=", x2)
