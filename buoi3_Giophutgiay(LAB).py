# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:46:21 2024

@author: UNHI
"""

# Viết chương trình cho phép nhập vào giờ, phút và giây theo định dạng hh:mm:ss. Hãy đổi ra giây và in kết quả ra màn hình.

time = input("Nhập vào giờ, phút và giây theo định dạng hh:mm:ss nhé: ")
try:
    gio, phut, giay = map(int, time.split(":")) 
except ValueError:
    print("Định dạng giờ phút giây không hợp lệ. Vui lòng nhập lại đúng định dạng")
else:
    if gio > 24 or gio < 0:
        print("Thời gian không hợp lệ. Vui lòng nhập lại")
    elif phut < 0 or phut >= 60:
        print("Thời gian không hợp lệ. Vui lòng nhập lại")
    elif giay < 0 or giay >= 60:
        print("Thời gian không hợp lệ. Vui lòng nhập lại")
    else:
        print("Tổng số giây là: ", gio*3600 + phut*60 + giay)