# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:47:37 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
# Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990)
a = int(input("Nhập ngày sinh:"))
b = int(input("Nhập tháng sinh:"))
c = int(input("Nhập năm sinh:"))
print(f"{a}/{b}/{c}")
# Ngày/Tháng/Năm (Nhập 20 8 1990 thì xuất 20/8/90)
a = int(input("Nhập ngày sinh: "))
b = int(input("Nhập tháng sinh: "))
c = int(input("Nhập năm sinh: "))
y = c % 100
print(f"{a}/{b}/{y}")
# Năm/tháng/ngày ("Nhập 20 8 1990 thì xuất 1990/8/20)
a = int(input("Nhập ngày sinh:"))
b = int(input("Nhạp tháng sinh:"))
c = int(input("Nhập năm sinh:"))
print(f"{c}/{b}/{a}")

