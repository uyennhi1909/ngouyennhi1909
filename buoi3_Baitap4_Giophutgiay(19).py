# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:25:33 2024

@author: UNHI
"""

#  Viết chương trình cho phép nhập vào giờ, phút và giây (ví dụ 8 39 50). Hãy đổi ra giây và in kết quả ra màn hình

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if gio >= 0  and gio < 24 and phut >= 1 and phut < 60 and giay >= 1 and giay < 60:
    print("Bây giờ là:", gio ,"giờ", phut ,"phút", giay ,"giây")
    x = gio*3600
    y = phut*60
    print("Tổng số giây là:",x+y+giay,"giây")
else:
    print("Nhập sai! Vui lòng nhập lại")