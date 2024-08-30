# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:43:00 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
a=input("Nhập giờ,phút,giây:")
gio,p,s=map(int,a.split(","))
if gio<24 and p<60 and s<=60:
    print(f"Thời gian là: {gio}:{p}:{s}")
else:
    print(a=input("Không hợp lệ,Nhập lại giờ,phút,giây:"))
