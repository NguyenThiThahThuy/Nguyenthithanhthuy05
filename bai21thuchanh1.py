# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:21:04 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
num=int(input("Nhập số:"))
chu=["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
n_c={0:"không",
     1:"một",
     2:"hai",
     3:"ba",
     4:"bốn",
     5:"năm",
     6:"sáu",
     7:"bảy",
     8:"tám",
     9:"chín"} 
if num in n_c:
    print(n_c[num])
else:
    print("Không đọc được  ")
    
    
