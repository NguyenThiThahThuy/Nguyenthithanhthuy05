# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:29:41 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
a=float(input("Nhập giá trị a:"))
b=float(input("Nhập giá trị b:"))
if a==0 and b==0:
    print ("phương trình vô nghiệm")
elif a==0 and b!=0:
    print ("phương trình vô số nghiệm")
else:
    print("Nghiệm của phương trình là x=",(-b/a))
    