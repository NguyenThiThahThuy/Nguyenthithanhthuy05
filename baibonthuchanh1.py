# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:59:58 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
N = int(input("Nhap so co 2 chu so:"))
if 10 <= N <= 99:
    hangchuc= N // 10
    hangdonvi= N % 10
    tong= hangchuc + hangdonvi
    print(f"Tong cac chu so cua N la: {hangchuc} + {hangdonvi}= {tong}")
else:
    print("Khong hop le")
